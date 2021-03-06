from DataMining import DataVisualization
from flask import Blueprint,request
import sqlite3
import pandas as pd
import json
import base64
import os

bp = Blueprint("DataVisualization",__name__)

DBdir = os.path.join(os.getcwd(),'Database','database.db')

@bp.route('/AgeWithBalance')
def AgeWithBalanceRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error":"É necessário ter um id para prosseguir"}),400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error":"Você não tem autorização para realizar essa operação."}),401

    Upload_Folder = os.path.join(os.getcwd(), 'Dataset')
    ListDirMined = os.listdir(os.path.join(Upload_Folder, 'Mined'))

    if len(ListDirMined) > 0:
        file_path = "./Dataset/Mined/"+ListDirMined[0]
        Bank_Data = pd.read_excel(file_path)
    else:
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.AgeWithBalance(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image':plot_url})


@bp.route('/AgeWithDuration')
def AgeWithDurationRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.AgeWithDuration(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400


    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/ClientsQuantityAge')
def ClientsQuantityRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.ClientsQuantityAge(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400


    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/AgeMarital')
def AgeMaritalRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.AgeMarital(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400


    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/JobsQuantity')
def JobsQuantityRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.JobsQuanity(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400


    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/BalanceWithJob')
def BalanceWithJobRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.BalanceWithJob(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400


    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/AgeWithLoan')
def AgeWithLoanRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.AgeWithLoan(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/AgeWithHousing')
def AgeWithHousingRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.AgeWithHousing(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/AgeWithDefault')
def AgeWithDefaultRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.AgeWithDefault(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/ContactWithDuration')
def ContactWithDurationRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.ContactWithDuration(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/ContactWithAge')
def ContactWithAgeRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412
    try:
        figure = DataVisualization.ContactWithAge(Bank_Data)
    except:
        return json.dumps({"error":"No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})

@bp.route('/StatusCampaign')
def StatusCampaignRoute():
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
        return json.dumps({"error":"Nenhum dataset pós mineração de dados foi encontrado"}),412

    try:
        figure = DataVisualization.StatusCampaign(Bank_Data)
    except:
        return json.dumps({"error": "No minimo uma das colunas requisitadas para criar este gráfico não foram encontradas, isso acontece porque ela estava mal-formatada ou tinha poucos dados"}),400

    plot_url = base64.b64encode(figure.getvalue()).decode('utf8')

    conn.close()

    return json.dumps({'image': plot_url})
