from flask import Flask, json
from flask_cors import CORS
from app.model.models import Livro, Usuario, Colecao
from app.controller.route import main
from app.data.config_db import Base, engine
from app.data.seed import seed_db
from app.config_jwt import jwt
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    Base.metadata.create_all(bind=engine)

    app.config["JWT_SECRET_KEY"] = "chave-super-secreta-que-nem-eu-mesmo-sei"
    app.config["JWT_HEADER_NAME"] = "autorizacao"	
    jwt.init_app(app)
    with open("./doc/swagger.json") as f:
        swagger_template = json.load(f)

    Swagger(app, template=swagger_template)
    
    CORS(
        app,
        resources={r"/*": {
            "origins": [
                "https://deleon-santos.github.io",
                "http://127.0.0.1:5500",
                "http://localhost:5500"
            ]
        }},
        supports_credentials=True
    )
    seed_db()
    
    return app