from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.data.config_db import Base

# 1. DEFINA A TABELA DE ASSOCIAÇÃO PRIMEIRO
# Ela precisa existir no topo do arquivo para que as classes abaixo a conheçam.
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
    autor_id = Column(Integer, ForeignKey("autores.autor_id"), nullable=False)
    autor_name = Column(String, nullable=False)  # NOVO CAMPO PARA O NOME DO AUTOR
    autor = relationship("Autor", back_populates="livros")
    
    # 2. USE A VARIÁVEL colecoes_livros (sem aspas) aqui
    colecoes = relationship("Colecao", secondary=colecoes_livros, back_populates="livros")


class Autor(Base):
    __tablename__ = "autores"
    autor_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    livros = relationship("Livro", back_populates="autor")


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
    
    # 3. USE A VARIÁVEL colecoes_livros aqui também
    livros = relationship("Livro", secondary=colecoes_livros, back_populates="colecoes")