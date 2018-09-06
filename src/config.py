# dev configuration
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    db_host = os.environ['POSTGRES_HOST']
    db_name = os.environ['POSTGRES_DB']
    db_user = os.environ['POSTGRES_USER']
    db_pass = os.environ['POSTGRES_PASSWORD']
    db_port = os.environ['POSTGRES_PORT']

    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SENTRY_DSN = '__YOUR_SENTRY_DSN_HERE__'


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}
