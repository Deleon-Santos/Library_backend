from flask import Blueprint, render_template, request
from app.model.models import Livro, Usuario
from app.service.services import  adicionar_novo_livro, autenticar_usuario, pegar_colections, pegar_favoritos

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    
    usuario = Usuario(
        email=data["email"], 
        senha=data["senha"]
                         )
    return autenticar_usuario(usuario)
    



@main.route("/add_favoritos/<int:colection_id>", methods=["POST"])
def add_favoritos(colection_id):
    data = request.get_json()
    print(data)						
    novo_favorito = Livro(
        titulo=data["titulo"],
        ano=data["ano"],
        descricao=data["descricao"],
        autor=data["autor"],
        capa=data["capa"]
    )

    return adicionar_novo_livro(novo_favorito, colection_id)


@main.route("/mostrar_favoritos/<int:colection_id>", methods=["GET"])
def mostrar_favoritos(colection_id):
    return pegar_favoritos(colection_id)


@main.route("/colections", methods=["GET"])
def colections():
    return pegar_colections()