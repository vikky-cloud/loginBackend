# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:password@localhost/loginDB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
