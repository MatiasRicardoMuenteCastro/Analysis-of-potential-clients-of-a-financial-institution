from werkzeug.utils import secure_filename
from flask import Blueprint
from flask import request
import sqlite3
import json
import os

DBdir = os.path.join(os.getcwd(),'Database','database.db')

allowed_extensions = 'xlsx'
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

Upload_Folder = os.path.join(os.getcwd(),'Dataset')

bpFiles = Blueprint('Files',__name__)


@bpFiles.route('/Upload',methods = ["POST"])
def UploadDataset():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error":"É necessário ter um id para prosseguir"}),400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error":"Você não tem autorização para realizar essa operação."}),401

    if 'excel' not in request.files:
        return ({'error':'Nenhum arquivo foi encontrado'}),400

    File = request.files['excel']  #Colocar esse mesmo nome em name no html na hora de fazer o input

    if File.filename == '':
        return ({'error': 'Nenhum arquivo foi selecionado'}),400

    ListDir = os.listdir(os.path.join(Upload_Folder,'Brute'))

    if File and allowed_file(File.filename):
        if len(ListDir) > 0:
            os.remove(os.path.join(Upload_Folder, 'Brute', secure_filename(ListDir[0])))

        File.filename.rsplit('.', 1)[1].lower()
        SavePath = os.path.join(Upload_Folder,'Brute',secure_filename(File.filename))
        File.save(SavePath)

        return ({'sucess': 'Upload feito com sucesso'})
    else:
        return ({'error': 'O arquivo deve ter a extensão do excel xlsx'}),400
