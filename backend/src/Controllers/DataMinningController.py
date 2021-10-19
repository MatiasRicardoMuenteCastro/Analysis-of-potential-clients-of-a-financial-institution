from backend.src.DataMining.DataPreparation import Data_Preparation
from werkzeug.utils import secure_filename
from flask import Blueprint,request
import pandas as pd
import sqlite3
import json
import os

DBdir = os.path.join(os.getcwd(),'Database','database.db')

Upload_Folder = os.path.join(os.getcwd(),'Dataset')

bpDM = Blueprint('Data Mining',__name__)

@bpDM.route('/Data_Mining', methods = ["PUT"])
def Data_Mining():
    try:
        conn = sqlite3.connect(DBdir, check_same_thread=False)
        cursor = conn.cursor()

        UserId = request.headers.get("id")

        if not UserId:
            return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

        cursor.execute(f"select user_id from users where user_id = '{UserId}'")
        userIdFind = cursor.fetchall()

        if not userIdFind:
            return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

        ListDirBrute = os.listdir(os.path.join(Upload_Folder, 'Brute'))

        ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

        path = './Dataset/Brute/'+ListDirBrute[0]

        Brute_Data = pd.read_excel(path)
        Bank_Data = Data_Preparation(Brute_Data)

        if len(ListDirMined) > 0:
            os.remove(os.path.join(Upload_Folder, 'Mined', secure_filename(ListDirMined[0])))

        Bank_Data.to_excel('./Dataset/Mined/Bank_Data.xlsx', index=False)

        conn.close()

        return ({'sucess':'A mineração de dados foi concluida'})
    except:
        return ({'error': 'Por favor faça o upload de um dataset compátivel com o modelo de mineração'}),400