from flask import Blueprint,request
from py_essentials import simpleRandom as sr
import sqlite3
import bcrypt
import json
import os

DBdir = os.path.join(os.getcwd(),'Database','database.db')

bpUser = Blueprint('User',__name__)

@bpUser.route("/user/delete", methods = ["DELETE"])
def UserDelete():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserJson = request.get_json(force=True)
    UserId = request.headers.get("id")

    try:
        UserJson['user_id']
    except:
        return json.dumps({"error": "Preencha a requisição com os dados indicados."}), 400

    if not UserId:
        return json.dumps({"error": "É necessário ter um id para prosseguir"}), 400

    if UserJson['user_id'] == "":
        return json.dumps({"error": "Por favor preencha o campo requisitado."}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    cursor.execute(f"select user_id from users where user_id = '{UserJson['user_id']}'")
    userIdDeleteFind = cursor.fetchall()

    if not userIdDeleteFind:
        return json.dumps({"error":"O usuário que você deseja deletar não foi encontrado."}),412

    [user_id] = userIdFind
    [id_delete] = userIdDeleteFind

    if user_id[0] == id_delete[0]:
        return json.dumps({"error":"Você não pode deletar a conta em que está logado."}),412

    cursor.execute(f"delete from users where user_id = '{UserJson['user_id']}'")

    conn.commit()
    conn.close()

    return json.dumps({"sucess":"O usuário foi removido com sucesso!"})

@bpUser.route("/session",methods = ["POST"])
def SessionRoute():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserJson = request.get_json(force=True)

    try:
        UserJson['user']
        UserJson['password']
    except:
        return json.dumps({"error":"Preencha a requisição com os dados indicados."}),400

    if UserJson['user'] == "" or UserJson['password'] == "":
        return json.dumps({"error":"Por favor preencha os campos requisitados."}),400

    cursor.execute(f"select user from users where user = '{UserJson['user']}'")
    userNameFind = cursor.fetchall()

    if not userNameFind:
        return json.dumps({"error": "Nome de usuário não existente"}), 401

    cursor.execute(f"select password from users where user = '{UserJson['user']}'")
    [userPasswordFind] = cursor.fetchall()
    password = userPasswordFind[0]

    if not bcrypt.checkpw(UserJson['password'].encode("utf-8"),password):
        return json.dumps({"error":"Senha inválida"}),401

    cursor.execute(f"select user_id from users where user = '{UserJson['user']}'")
    [[user_id]] = cursor.fetchall()

    return json.dumps({"id": user_id, "user": UserJson['user']})

@bpUser.route('/user/create', methods=["POST"])
def UserCreate():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserJson = request.get_json(force=True)
    UserId = request.headers.get("id")

    try:
        UserJson['user']
        UserJson['password']
    except:
        return json.dumps({"error":"Preencha a requisição com os dados indicados."}),400

    if not UserId:
        return json.dumps({"error":"É necessário ter um id para prosseguir"}),400

    if UserJson['user'] == "" or UserJson['password'] == "":
        return json.dumps({"error":"Por favor preencha os campos requisitados."}),400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error":"Você não tem autorização para realizar essa operação."}),401

    cursor.execute(f"select user from users where user = '{UserJson['user']}'")
    userNameFind = cursor.fetchall()

    if userNameFind:
        return json.dumps({"error":"Nome de usuário já existente"}),406

    id = sr.randomString(10)
    salt = bcrypt.gensalt(12)
    password = bcrypt.hashpw(UserJson['password'].encode("utf-8"),salt)

    cursor.execute("""
             INSERT INTO users (user_id,user,password)
             VALUES(?,?,?)
        """,(id, UserJson['user'], password))

    conn.commit()
    conn.close()

    return json.dumps({"id": id, "user": UserJson['user']})

@bpUser.route("/users", methods = ["GET"])
def UsersIndex():
    conn = sqlite3.connect(DBdir, check_same_thread=False)
    cursor = conn.cursor()

    UserId = request.headers.get("id")

    if not UserId:
        return json.dumps({"error": "É necessario ter um id para prosseguir"}), 400

    cursor.execute(f"select user_id from users where user_id = '{UserId}'")
    userIdFind = cursor.fetchall()

    if not userIdFind:
        return json.dumps({"error": "Você não tem autorização para realizar essa operação."}), 401

    cursor.execute(f"select user_id,user from users")
    usersList = cursor.fetchall()

    conn.close()

    return json.dumps({"usuarios":usersList})


