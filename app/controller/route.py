from flask import Blueprint, jsonify, render_template, request
from app.model.models import Colecao, Livro, Usuario
from app.service.services import  adicionar_novo_livro, autenticar_usuario, criar_colecao, excluir_colection, excluir_livro, novo_cadastro_usuario, pegar_colections, pegar_favoritos
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
def cadastrar_usuario():

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


@main.route("/add_livro/<int:colection_id>", methods=["POST"])
@jwt_required()
def add_favoritos(colection_id):
    user_jwt = int(get_jwt_identity())
    print(f"impressão dos dados auteticads do usuario {user_jwt}")
    
    data = request.get_json()
    print(f"dados recebidos do fronte , {data}")
    	
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


@main.route("/mostrar_livros/<int:colection_id>", methods=["GET"])
@jwt_required()
def mostrar_favoritos(colection_id):
    
    user_jwt= int(get_jwt_identity())
    if not user_jwt:
        return jsonify({
        "error": "Token inválido ou mal formatado"
        
    }), 422
    return pegar_favoritos(colection_id)


@main.route("/mostrar_colecao", methods=["GET"])
@jwt_required()
def colections():
    user_jwt = int(get_jwt_identity())
    if not user_jwt:
        return jsonify({"erro":"Autor não indentificado"}),401
    return pegar_colections(user_jwt)


@main.route("/nova_colecao", methods=["POST"])
@jwt_required()
def criar_nova_colecao():
    user_jwt = int(get_jwt_identity())
    if not user_jwt:
        return jsonify({"erro":"Autor não indentificado"}),401

    data = request.get_json()
    if not data.get("nome"):
        return jsonify({"erro":"Nome da coleção não foi informado"})

    colecao = Colecao(
        nome = data["nome"],
        usuario_id = user_jwt
    )
    return criar_colecao(colecao, user_jwt)


@main.route("/deletar_colecao/<int:colection_id>", methods=["DELETE"])
@jwt_required()
def delete_colection_route(colection_id):
    user_jwt = int(get_jwt_identity())
    if not user_jwt:
        return jsonify({"erro":"Autor não indentificado"}),401
    return excluir_colection(colection_id, user_jwt)


@main.route("/deletar_livro/<int:livro_id>", methods=["DELETE"])
@jwt_required()
def deletar_livro(livro_id):
    user_jwt = int(get_jwt_identity())
    if not user_jwt:
        return jsonify({"erro":"Autor não indentificado"}),401
    return excluir_livro(livro_id, user_jwt)
