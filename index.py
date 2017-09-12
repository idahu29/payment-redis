from flask import Flask
from config import BaseConfig
from application.api.paypal_payment import paypal
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# db = SQLAlchemy(app)
from database import DB
import logging

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
app.register_blueprint(paypal)
app.config.from_object(BaseConfig)
app.logger.setLevel(logging.INFO)
db = DB()
# bcrypt = Bcrypt(app)
