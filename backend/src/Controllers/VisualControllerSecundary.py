from backend.src.DataMining import DataVisualizationSecondary
from backend.src.PyAuth.authenticate import token_required
from flask import Blueprint
import pandas as pd
import json
import base64
import os

bp2 = Blueprint('DataVisualizationSecundary',__name__)

@bp2.before_request
@token_required

@bp2.route('/BalanceWithBlueCollar')
def BalanceBlueCollarRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithBlueCollar(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithRetired')
def BalanceRetiredRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithRetired(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithManagement')
def BalanceManagementRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithManagement(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithTechnician')
def BalanceTechnicianRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithTechnician(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithAdmin')
def BalanceAdminRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithAdmin(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithServices')
def BalanceServicesRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithServices(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})