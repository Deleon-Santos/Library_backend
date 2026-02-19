from .config import Config
from flask import Flask
# from .extensao import db, jwt

def appCreate():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY'] = "minha senha supersecreta que todos ja sabem"
    


    return app