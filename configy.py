import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'It is a secret cannot be told'
