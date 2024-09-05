import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '45UP3R53CR3TK3Y'
    # Set the path to the local 'data' folder
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASEDIR, "data", "upkeephub.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
