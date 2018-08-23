# coding:utf8

from flask import Flask
from configy import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes , models
