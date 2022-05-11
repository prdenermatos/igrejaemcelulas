# Módulo com as operações do banco de dados


from flask_mysqldb import MySQL

class CadastroMembroDB:
    def __init__(self, db):
        self.db = db
    # CREATE (INSERT)

