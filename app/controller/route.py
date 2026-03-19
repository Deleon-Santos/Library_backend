from flask import Blueprint, jsonify, render_template, request
from app.model.models import Colecao, Livro, Usuario
from app.service.services import  adicionar_novo_livro, autenticar_usuario, criar_colecao, excluir_colection, novo_cadastro_usuario, pegar_colections, pegar_favoritos
from flask_jwt_extended import jwt_required, get_jwt_identity
import bcrypt
main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data.get("email") or not data.get("senha"):
        return jsonify({"error": "Dados inválidos"}), 400
       
    usuario = Usuario(
        email=data["email"], 
        senha=data["senha"]
                         )
    return autenticar_usuario(usuario)
    

@main.route("/cadastro", methods=["POST"])
def cadastrar_usuaario():

    data = request.get_json()
    if not data.get("email") or not data.get("senha"):
        return jsonify({"error": "Dados inválidos"}), 400
    
    senha_hash = bcrypt.hashpw(data["senha"].encode("utf-8"), bcrypt.gensalt())
    novo_usuario= Usuario(
        nome = data["nome"],
        email = data["email"],
        senha=senha_hash.decode("utf-8")
    )
    return novo_cadastro_usuario(novo_usuario)


@main.route("/add_favoritos/<int:colection_id>", methods=["POST"])
@jwt_required()
def add_favoritos(colection_id):
    user_jwt = get_jwt_identity()
    
    data = request.get_json()
    print(data)	
    campos = ["titulo", "ano", "descricao", "autor", "capa"]
    if not all(campo in data for campo in campos):
        return jsonify({"error": "Dados incompletos"}), 400
					
    novo_favorito = Livro(
        titulo=data["titulo"],
        ano=data["ano"],
        descricao=data["descricao"],
        autor=data["autor"],
        capa=data["capa"]
    )
    return adicionar_novo_livro(novo_favorito, colection_id, user_jwt)


@main.route("/mostrar_favoritos/<int:colection_id>", methods=["GET"])
def mostrar_favoritos(colection_id):
    return pegar_favoritos(colection_id)


@main.route("/colections", methods=["GET"])
def colections():
    return pegar_colections()


@main.route("/nova_colecao", methods=["POST"])
def criar_nova_colecao():
    data = request.get_json()
    colecao = Colecao(
        nome = data["nome"],
        usuario_id = data["usuario_id"] 
    )
    return criar_colecao(colecao)


@main.route("/delete_colection/<int:colection_id>", methods=["DELETE"])
def delete_colection_route(colection_id):
    return excluir_colection(colection_id)

