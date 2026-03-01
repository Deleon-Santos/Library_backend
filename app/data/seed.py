from app.model.models import  Livro, Usuario, Colecao

from .config_db import Session

def seed_db():
    with Session()as session:
        if session.query(Livro).first():
            return
        
        livro1 = Livro(titulo="Harry Potter e a Pedra Filosofal", ano=1997, descricao="O primeiro livro da série Harry Potter.", autor="J.K. Rowling",capa=7239831)
        livro2 = Livro(titulo="A Guerra dos Tronos", ano=1996, descricao="O primeiro livro da série As Crônicas de Gelo e Fogo.", autor="George R.R. Martin", capa=7239832)
        session.add_all([livro1, livro2])       

        usuario1 = Usuario(nome="Alice", email="alice@.com", senha="senha123")
        usuario2 = Usuario(nome="Bob", email="bob@.com", senha="senha456")
        session.add_all([usuario1, usuario2])
        session.commit()    

        coleção1 = Colecao(nome="Romance", usuario_id=usuario1.usuario_id)
        coleção2 = Colecao(nome="Fantasia", usuario_id=usuario2.usuario_id)
        session.add_all([coleção1, coleção2])   


        session.commit()
        