import  os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "mubina12"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'movies.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False