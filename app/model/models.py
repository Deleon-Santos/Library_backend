from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.data.config_db import Base


colecoes_livros = Table(
    "colecoes_livros", # Nome no Banco de Dados
    Base.metadata,
    Column("colecao_id", Integer, ForeignKey("colecoes.colecao_id"), primary_key=True),
    Column("livro_id", Integer, ForeignKey("livros.livro_id"), primary_key=True)
)


class Livro(Base):
    __tablename__ = "livros"
    livro_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    descricao = Column(String, nullable=False)
    autor = Column(String, nullable=False)  
    
    colecoes = relationship("Colecao", secondary=colecoes_livros, back_populates="livros")


class Usuario(Base):
    __tablename__ = "usuarios"
    usuario_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    
    colecoes = relationship("Colecao", back_populates="usuario")


class Colecao(Base):
    __tablename__ = "colecoes"
    colecao_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=False)
 
    usuario = relationship("Usuario", back_populates="colecoes")    
    livros = relationship("Livro", secondary=colecoes_livros, back_populates="colecoes")