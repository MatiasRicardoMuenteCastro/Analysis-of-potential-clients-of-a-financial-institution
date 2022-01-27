from Controllers.VisualController import bp
from Controllers.VisualControllerSecundary import bp2
from Controllers.UserController import bpUser
from Controllers.FilesController import bpFiles
from Controllers.DataMinningController import bpDM

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(bp)
app.register_blueprint(bp2)
app.register_blueprint(bpUser)
app.register_blueprint(bpFiles)
app.register_blueprint(bpDM)

app.run(debug = True)