from flask import Flask
from config import BaseConfig
from application.api.paypal_payment import paypal_payment
from application.api.braintree_payment import braintree_payment
from application.api.stripe_payment import stripe_payment

# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# db = SQLAlchemy(app)
from database import DB
import logging

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
app.register_blueprint(paypal_payment)
app.register_blueprint(braintree_payment)
app.register_blueprint(stripe_payment)
app.config.from_object(BaseConfig)
app.logger.setLevel(logging.INFO)
db = DB()
# bcrypt = Bcrypt(app)
