from app.model.models import Autor, Livro, Usuario, Colecao

from .config_db import Session

def seed_db():
    with Session()as session:
        if session.query(Autor).first():
            return
        autor1 = Autor(nome="J.K. Rowling")
        autor2 = Autor(nome="George R.R. Martin")
        session.add_all([autor1, autor2])
        session.commit()

        livro1 = Livro(titulo="Harry Potter e a Pedra Filosofal", ano=1997, descricao="O primeiro livro da série Harry Potter.", autor_id=autor1.autor_id)
        livro2 = Livro(titulo="A Guerra dos Tronos", ano=1996, descricao="O primeiro livro da série As Crônicas de Gelo e Fogo.", autor_id=autor2.autor_id)
        session.add_all([livro1, livro2])       

        usuario1 = Usuario(nome="Alice", email="alice@example.com", senha="senha123")
        usuario2 = Usuario(nome="Bob", email="bob@example.com", senha="senha456")
        session.add_all([usuario1, usuario2])
        session.commit()    

        coleção1 = Colecao(nome="Romance", usuario_id=usuario1.usuario_id)
        coleção2 = Colecao(nome="Fantasia", usuario_id=usuario2.usuario_id)
        session.add_all([coleção1, coleção2])   


        session.commit()
        