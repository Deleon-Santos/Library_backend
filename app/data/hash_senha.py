import bcrypt

def gerar_hash_senha(senha: str) -> str:
    salt = bcrypt.gensalt()
    hash_senha = bcrypt.hashpw(senha.encode("utf-8"), salt)
    return hash_senha.decode("utf-8")