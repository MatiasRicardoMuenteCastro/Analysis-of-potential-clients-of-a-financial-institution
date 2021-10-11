from flask import Blueprint
import json
import jwt
import datetime
from hashlib import sha256
import random

bpSession = Blueprint('Session',__name__)

SECRET_KEY = "2191C4907FB69F2F698C214C164D1D1F8716739CAC1E1B82B663C3B7D9B98E5A"

@bpSession.route('/Session', methods=["POST"])
def Session():
     randomNumber = random.randrange(10**80)
     hash256 = sha256(str(randomNumber).encode('UTF-8')).hexdigest()
     timeLimit = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
     Token = jwt.encode({'Token':hash256,'exp': timeLimit}, SECRET_KEY, algorithm='HS256')
     return json.dumps({"Token":Token})