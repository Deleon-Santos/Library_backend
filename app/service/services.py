from flask import jsonify
from app.data.config_db import Session
from app.model.models import  Colecao, Usuario

def adicionar_novo_livro(novo_favorito,colection_id):
    try:
        with Session() as session:
            session.add(novo_favorito)
            session.commit()
            session.refresh(novo_favorito)
        
            colecao = session.query(Colecao).filter_by(colecao_id=colection_id).first()

            if not colecao:
                return jsonify({"error": "Coleção não encontrada"}), 404
            colecao.livros.append(novo_favorito)
            session.commit()
            session.refresh(novo_favorito)

            return jsonify({
                "id": colecao.colecao_id,
                "nome": colecao.nome,
                "livros": [
                    {
                        "id": livro.livro_id,
                        "titulo": livro.titulo,
                        "descricao": livro.descricao,
                        "autor": livro.autor,
                        "capa": livro.capa
                    }
                    for livro in colecao.livros
                ]
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

           
def pegar_favoritos(id):
    try:
        with Session() as session:
            colecao = session.query(Colecao).filter_by(colecao_id=id).first()

            if not colecao:
                return jsonify({"error": "Coleção não encontrada"}), 404

            return jsonify({
                "id": colecao.colecao_id,
                "nome": colecao.nome,
                "livros": [
                    {
                        "id": livro.livro_id,
                        "titulo": livro.titulo,
                        "descricao": livro.descricao,
                        "autor": livro.autor,
                        "capa": livro.capa
                    }
                    for livro in colecao.livros
                ]
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def pegar_colections():
    try:
        with Session() as session:
            colecoes = session.query(Colecao).all()
            return jsonify([
                {
                    "id": colecao.colecao_id,
                    "nome": colecao.nome
                }
                for colecao in colecoes
            ])
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def autenticar_usuario(usuario):
    try:
        with Session() as session:
            usuario_db = session.query(Usuario).filter_by(email=usuario.email, senha=usuario.senha).first()
            if usuario_db:
                return jsonify({"status": "ok", "usuario_id": usuario_db.usuario_id, "nome": usuario_db.nome})
            else:
                return jsonify({"error": "Credenciais inválidas"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500