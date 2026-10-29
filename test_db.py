import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
print(database_url)

if not database_url:
    print("❌ ERRO: A variável DATABASE_URL não foi encontrada!")
    exit(1)

# Ajusta o prefixo para usar o psycopg2 explicitamente
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif database_url.startswith("postgresql://") and "+psycopg2" not in database_url:
    database_url = database_url.replace("postgresql://", "postgresql+psycopg2://", 1)

print(f"🔄 Tentando conectar ao Supabase...")

try:
    engine = create_engine(database_url)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.fetchone()
        print("\n🎉 CONEXÃO BEM-SUCEDIDA!")
        print(f"Versão do Banco de Dados: {version[0]}")
except Exception as e:
    print("\n❌ FALHA NA CONEXÃO:")
    print(e)