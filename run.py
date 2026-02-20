from flask import Flask
from app.data.config_db import Base, engine
from app.data.seed import seed_db
# Importar os modelos garante que o Base conheça as tabelas
from app.model.models import Autor, Livro, Usuario, Coleção

def appCreate():
    app = Flask(__name__)
    
    # 1. Cria as tabelas
    Base.metadata.create_all(bind=engine)
    
    # 2. Alimenta o banco
    seed_db()
    
    return app

app = appCreate()

if __name__ == '__main__':
    app.run(debug=True)