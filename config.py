import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = None
    SQLALCHEMY_DATABASE_URI = None


class LocalConfig(Config):
    """ here, set any api keys or secrets that are not committed to git"""
    try:
        from local_env.secrets import SECRET_KEY, DATABASE_URL
        SECRET_KEY = SECRET_KEY
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    except:
        pass


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(LocalConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(LocalConfig):
    TESTING = True
