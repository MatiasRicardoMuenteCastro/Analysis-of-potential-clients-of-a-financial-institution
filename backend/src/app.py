from backend.src.Controllers.VisualController import bp
from backend.src.Controllers.VisualControllerSecundary import bp2
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(bp)
app.register_blueprint(bp2)

app.run(debug = True)