import os

from setup import basedir


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

PAYPAL_MODE='sandbox'   # sandbox or live
PAYPAL_CLIENT_ID='AZDea7NX3hwxn06oMt1-DkSUq2czSmEqcS45TYwImm7tlWNNXDxojf0U5gLQ6yz8-HW53_k7MKwE3d4S'
PAYPAL_CLIENT_SECRET='EKjXxlBc0TELhCpyJLJ6GjMRHp0D6xFg6eFrDBLrvESGMKpJVITjDtUDglaLTJSQRGMSNb3NiQbjDRAS'
