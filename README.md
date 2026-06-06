
# 📚 Library Back-end: Sistema de Gerenciamento de Coleções
![imagen](capa.png)
# Swagger 👉 [Acessar Deploy](https://library-backend-b4as.onrender.com/apidocs) 👈



  **Backend**
  Construido em Flask esta hospedado no Render(a versão free constuma hibernar e leva alguns segundo para retornar a disponibilidade)
  
  **Database**
  Hopedado no Supabase na versão gratuita

---

## 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologia | Ícone |
| :--- | :--- | :--- |
| **Linguagem Backend** | Python 3.12+ | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| **Framework Web** | Flask | ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) |
| **Banco de Dados** | PostgreSQL | ![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) |

---

## 🌐 Arquitetura de Dados e APIs

O projeto opera com um modelo triplo de integração de dados para garantir performance e escalabilidade:

### 1. 📖 OpenLibrary API (Pública)
Utilizada para o motor de busca global. Permite que o usuário encontre milhões de livros em tempo real consumindo metadados diretamente da [OpenLibrary](https://openlibrary.org/).

### 2. 📄 Camada JSON (Local)
Uma API local baseada em arquivos JSON estáticos para carregar dados de configuração, categorias pré-definidas e elementos de interface que não necessitam de processamento no banco de dados.

### 3. 🐍 Flask Collections API (Persistente)
Desenvolvida em **Flask**, esta API é responsável pelo CRUD (Criação, Leitura, Atualização e Deleção) das coleções dos usuários.
* **Conexão:** Integrada ao **PostgreSQL** através do driver `psycopg2-binary`.
* **Gerenciamento:** Armazena as preferências, bibliotecas salvas e status de leitura de cada usuário de forma segura.

---

## 🏗️ Implementações

* **Dominios:** Configuração de CORS para acesso restrito a dominios previamente autorizados
* **Documentação:** API documentada via Swagger
* **Autenticação e autorização:** Controle de usuario via JWT 
* **Backend:** Estrutura modular utilizando *Application Factory*  e separação de competencias(`create_app`).
* **Segurança:** Gerenciamento de chaves e strings de conexão via `python-dotenv`.
* **ORM:** Sqlamchemy para estruturar o banco de dados como objetos.
---

