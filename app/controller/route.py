from flask import Blueprint, render_template, request
from app.model.models import Livro
from service.services import adicionar_favorito, adicionar_novo_livro

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/salvar_livro", methods=["POST"])
def salvar_livro():
    data = request.get_json()

    novo_livro = Livro(
        titulo=data["titulo"],
        ano=data["ano"],
        descricao=data["descricao"],
        autor_id=data["autor_id"]
    )


    return adicionar_novo_livro(novo_livro)


@main.route("/add_favoritos/<int:colection_id>", methods=["POST"])
def add_favoritos(colection_id):
    data = request.get_json()
    novo_favorito = Livro(
        titulo=data["titulo"],
        ano=data["ano"],
        descricao=data["descricao"],
        autor_id=data["autor_id"]
    )


    return adicionar_favorito(novo_favorito, colection_id)
    