from flask import Flask,request
import jwt
import json


flask_app = Flask(__name__)

SECRET_KEY = "2191C4907FB69F2F698C214C164D1D1F8716739CAC1E1B82B663C3B7D9B98E5A"

def token_required(something):
    def wrap():
        try:
            token_passed = request.headers['TOKEN']
            if request.headers['TOKEN'] != '' and request.headers['TOKEN'] != None:
                try:
                    data = jwt.decode(token_passed,SECRET_KEY, algorithms=['HS256'])
                    return something()
                except jwt.exceptions.ExpiredSignatureError:
                    return_data = {
                        "message": "O Token expirou"
                        }
                    return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json'),401
                except:
                    return_data = {
                        "message": "Token inválido"
                    }
                    return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json'),401
            else:
                return_data = {
                    "message" : "É necessário um token de autenticação",
                }
                return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json'),401
        except Exception as e:
            return_data = {
                "message" : "Ocorreu um erro na validação do token"
                }
            return flask_app.response_class(response=json.dumps(return_data), mimetype='application/json'),500

    return wrap