from flask import jsonify
from app.data.config_db import Session
from app.model.models import Colecao

def adicionar_novo_livro(novo_livro):
    try:
        with Session() as session:
            session.add(novo_livro)
            session.commit()
            session.refresh(novo_livro)

            return jsonify({
                "id_livro": novo_livro.livro_id,
                "titulo": novo_livro.titulo,
                "ano": novo_livro.ano,
                "descricao": novo_livro.descricao,
                "autor_id": novo_livro.autor_id
            }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def adicionar_favorito(novo_favorito,colection_id):
    try:
        with Session() as session:
            colecao = session.query(Colecao).filter_by(colecao_id=colection_id).first()
            if not colecao:
                return jsonify({"error": "Coleção não encontrada"}), 404
            
            colecao.livros.append(novo_favorito)
            session.commit()
            session.refresh(novo_favorito)

            return jsonify({
    "id": colecao.colecao_id,
    "nome": colecao.nome
}), 200 
        

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
                        "descricao": livro.descricao
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