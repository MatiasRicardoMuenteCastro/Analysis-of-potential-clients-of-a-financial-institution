from backend.src.DataMining import DataVisualizationSecondary
from flask import Blueprint
import pandas as pd
import json
import base64


bp2 = Blueprint('DataVisualizationSecundary',__name__)

@bp2.route('/BalanceWithBlueCollar')
def BalanceBlueCollarRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualizationSecondary.BalanceWithBlueCollar(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithRetired')
def BalanceRetiredRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualizationSecondary.BalanceWithRetired(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithManagement')
def BalanceManagementRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualizationSecondary.BalanceWithManagement(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithTechnician')
def BalanceTechnicianRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualizationSecondary.BalanceWithTechnician(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithAdmin')
def BalanceAdminRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualizationSecondary.BalanceWithAdmin(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithServices')
def BalanceServicesRoute():
    try:
        file_path = "../Dataset/Bank_Data.xlsx"
        Bank_Data = pd.read_excel(file_path)
    except:
        return json.dumps({'error': 'Por favor faça o upload de um Dataset'}), 412

    figure = DataVisualizationSecondary.BalanceWithServices(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')
    return json.dumps({'image': plot_url})