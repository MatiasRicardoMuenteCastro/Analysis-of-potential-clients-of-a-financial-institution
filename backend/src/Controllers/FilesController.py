from backend.src.PyAuth.authenticate import token_required
from werkzeug.utils import secure_filename
from flask import Blueprint
from flask import request
import os

allowed_extensions = 'xlsx'
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

Upload_Folder = os.path.join(os.getcwd(),'Dataset')

bpFiles = Blueprint('Files',__name__)


@bpFiles.route('/Upload',methods = ["POST"])
@token_required
def UploadDataset():

    if 'excel' not in request.files:
        return ({'error':'Nenhum arquivo foi encontrado'}),400

    File = request.files['excel']  #Colocar esse mesmo nome em name no html na hora de fazer o input

    if File.filename == '':
        return ({'error': 'Nenhum arquivo foi selecionado'}),400

    ListDir = os.listdir(os.path.join(Upload_Folder,'Brute'))

    if len(ListDir) > 0:
        os.remove(os.path.join(Upload_Folder,'Brute',secure_filename(ListDir[0])))

    if File and allowed_file(File.filename):
        File.filename.rsplit('.', 1)[1].lower()
        SavePath = os.path.join(Upload_Folder,'Brute',secure_filename(File.filename))
        File.save(SavePath)

        return ({'sucess': 'Upload feito com sucesso'})
    else:
        return ({'error': 'O arquivo deve ter a extensão do excel xlsx'}),400
