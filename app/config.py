import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
