import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # uri for postgres local database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')