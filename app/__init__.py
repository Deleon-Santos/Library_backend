from flask import Flask
from app.model.models import Autor, Livro, Usuario, Colecao
from app.controller.route import main
from app.data.config_db import Base, engine
from app.data.seed import seed_db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    Base.metadata.create_all(bind=engine)
    seed_db()
    
    return app