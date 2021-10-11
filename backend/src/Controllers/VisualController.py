from backend.src.DataMining import DataVisualization
from backend.src.PyAuth.authenticate import token_required
from flask import Blueprint
import pandas as pd
import json
import base64
import os

bp = Blueprint("DataVisualization",__name__)

@bp.before_request
@token_required

@bp.route('/AgeWithBalance')
def AgeWithBalanceRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.AgeWithBalance(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image':plot_url})


@bp.route('/AgeWithDuration')
def AgeWithDurationRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.AgeWithDuration(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/ClientsQuantityAge')
def ClientsQuantityRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.ClientsQuantityAge(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeMarital')
def AgeMaritalRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.AgeMarital(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/JobsQuantity')
def JobsQuantityRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.JobsQuanity(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/BalanceWithJob')
def BalanceWithJobRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.BalanceWithJob(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeWithLoan')
def AgeWithLoanRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.AgeWithLoan(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeWithHousing')
def AgeWithHousingRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.AgeWithHousing(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeWithDefault')
def AgeWithDefaultRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.AgeWithDefault(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/ContactWithDuration')
def ContactWithDurationRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.ContactWithDuration(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/ContactWithAge')
def ContactWithAgeRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.ContactWithAge(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/StatusCampaign')
def StatusCampaignRoute():
    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualization.StatusCampaign(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

