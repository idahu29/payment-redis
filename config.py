import os
import json
from setup import basedir

PROJECT_NAME="Payment Test"
PAYMENT_MODE = "sandbox"
with open('payment.json') as payment_file:
    PAYMENT=json.load(payment_file)

    PAYPAL = PAYMENT['paypal'][PAYMENT_MODE]
    BRAINTREE = PAYMENT['braintree'][PAYMENT_MODE]
    STRIPE = PAYMENT['stripe'][PAYMENT_MODE]



class BaseConfig(object):
    SECRET_KEY = "SO_SECURE"
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(object):
    """Development configuration."""
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG_TB_ENABLED = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

