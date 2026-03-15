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
    

def novo_cadastro_usuario(novo_usuario):
    try:
        with Session() as session:
            if session.query(Usuario).filter_by(email=novo_usuario.email).first():
                return jsonify({"error": "Email já cadastrado"}), 400
            session.add(novo_usuario)
            session.commit()
            session.refresh(novo_usuario)
            return jsonify({"status": "ok", "usuario_id": novo_usuario.usuario_id, "nome": novo_usuario.nome})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def criar_colecao(colecao):
    try: 
        with Session() as session:
            if session.query(Colecao).filter_by(nome=colecao.nome).first():
                return jsonify({"error": "Coleção já existe"}), 400
            session.add (colecao)
            session.commit()
            session.refresh(colecao)
            return jsonify({"status": "ok", "colecao_id": colecao.colecao_id, "nome": colecao.nome})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

def excluir_colection(colection_id):
    with Session() as session:
        try:
            colecao= session.query(Colecao).filter_by(colecao_id=colection_id).first()
            if not colecao:
                return jsonify({"error": "Coleção não encontrada"}), 404
            session.delete(colecao)
            session.commit()
            return jsonify({"ok": "Coleção removida!"}), 200
        except Exception as e:
            return jsonify({f"error": str(e)}), 500
        

