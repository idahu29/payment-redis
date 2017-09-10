from flask import Flask
from config import BaseConfig
from database import DB
# from flask_bcrypt import Bcrypt

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
app.config.from_object(BaseConfig)
db = DB()
# bcrypt = Bcrypt(app)
