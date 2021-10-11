from backend.src.DataMining.DataPreparation import Data_Preparation
from backend.src.PyAuth.authenticate import token_required
from werkzeug.utils import secure_filename
from flask import Blueprint
import pandas as pd
import os

Upload_Folder = os.path.join(os.getcwd(),'Dataset')

bpDM = Blueprint('Data Mining',__name__)

@bpDM.route('/Data_Mining', methods = ["PUT"])
@token_required
def Data_Mining():
    try:
        ListDirBrute = os.listdir(os.path.join(Upload_Folder, 'Brute'))

        ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

        if len(ListDirMined) > 0:
            os.remove(os.path.join(Upload_Folder, 'Mined', secure_filename(ListDirMined[0])))

        path = './Dataset/Brute/'+ListDirBrute[0]

        Brute_Data = pd.read_excel(path)
        Bank_Data = Data_Preparation(Brute_Data)

        Bank_Data.to_excel('./Dataset/Mined/Bank_Data.xlsx', index=False)
        return ({'sucess':'A mineração de dados foi concluida'})
    except:
        return ({'error': 'Por favor faça o upload de um dataset compátivel com o modelo de mineração'}),400