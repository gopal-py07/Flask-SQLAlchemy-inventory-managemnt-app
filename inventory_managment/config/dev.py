import os
from dotenv import load_dotenv

load_dotenv()

class DevConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_TRACK_MODIFICARIOM = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key-for-dev')

