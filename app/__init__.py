# coding:utf8

from flask import Flask
from configy import Config

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config['SECRET_KEY'])
from app import routes