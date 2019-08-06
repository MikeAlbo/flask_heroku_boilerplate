import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = SECRET_KEY or None  # 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    from session.config import SECRET_KEY, DATABASE_URL
    print("In Development Mode...")
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = DATABASE_URL  # 'DATABASE_URL'


class TestingConfig(Config):
    TESTING = True
