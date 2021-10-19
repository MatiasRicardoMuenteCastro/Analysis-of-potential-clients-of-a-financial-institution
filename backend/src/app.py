from backend.src.Controllers.VisualController import bp
from backend.src.Controllers.VisualControllerSecundary import bp2
from backend.src.Controllers.UserController import bpUser
from backend.src.Controllers.FilesController import bpFiles
from backend.src.Controllers.DataMinningController import bpDM

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