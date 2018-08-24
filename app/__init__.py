# coding:utf8

from flask import Flask
from configy import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_script import Manager, Server

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))
if __name__ == "__main__":
    manager.run()
from app import routes, models
