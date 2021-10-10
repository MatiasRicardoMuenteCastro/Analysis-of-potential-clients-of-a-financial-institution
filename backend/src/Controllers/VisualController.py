from backend.src.DataMining import DataVisualization
from flask import Blueprint
import pandas as pd
import json
import base64

bp = Blueprint("DataVisualization",__name__)

@bp.route('/AgeWithBalance')
def AgeWithBalanceRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error':'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.AgeWithBalance(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image':plot_url})

@bp.route('/AgeWithDuration')
def AgeWithDurationRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error':'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.AgeWithDuration(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/ClientsQuantityAge')
def ClientsQuantityRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.ClientsQuantityAge(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeMarital')
def AgeMaritalRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.AgeMarital(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/JobsQuantity')
def JobsQuantityRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.JobsQuanity(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/BalanceWithJob')
def BalanceWithJobRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.BalanceWithJob(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeWithLoan')
def AgeWithLoanRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.AgeWithLoan(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeWithHousing')
def AgeWithHousingRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.AgeWithHousing(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/AgeWithDefault')
def AgeWithDefaultRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.AgeWithDefault(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/ContactWithDuration')
def ContactWithDurationRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.ContactWithDuration(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/ContactWithAge')
def ContactWithAgeRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.ContactWithAge(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp.route('/StatusCampaign')
def StatusCampaignRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualization.StatusCampaign(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

