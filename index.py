from flask import Flask
from config import BaseConfig
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# db = SQLAlchemy(app)
from database import DB

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
app.config.from_object(BaseConfig)
db = DB()
# bcrypt = Bcrypt(app)
