import os

basedir = os.path.abspath(os.path.dirname(__file__))


# print(basedir)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'It is a secret cannot be told'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
