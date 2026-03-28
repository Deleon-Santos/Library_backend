from flask_jwt_extended import JWTManager


jwt = JWTManager()

# swagger_template = {
#     "openapi": "2.0",
#     "info": {
#         "title": "Library Backend API",
#         "version": "1.0.0",
#         "description": "API para gerenciamento de usuários, coleções e livros favoritos com JWT"
#     }
# }