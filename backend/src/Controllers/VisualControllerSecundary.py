from backend.src.DataMining import DataVisualizationSecondary
from flask import Blueprint,request
import sqlite3
import pandas as pd
import json
import base64
import os

bp2 = Blueprint('DataVisualizationSecundary',__name__)

DBdir = os.path.join(os.getcwd(),'Database','database.db')

@bp2.route('/BalanceWithBlueCollar')
def BalanceBlueCollarRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithBlueCollar(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithRetired')
def BalanceRetiredRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithRetired(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithManagement')
def BalanceManagementRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithManagement(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithTechnician')
def BalanceTechnicianRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithTechnician(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithAdmin')
def BalanceAdminRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithAdmin(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp2.route('/BalanceWithServices')
def BalanceServicesRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset de mineração foi encontrado"}),412

    figure = DataVisualizationSecondary.BalanceWithServices(Bank_Data)
    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})