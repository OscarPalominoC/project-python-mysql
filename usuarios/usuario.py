from database import db_connection
from datetime import datetime
import hashlib

connection = db_connection()
cursor = connection.cursor(buffered=True)

class Usuario:

    def __init__(self, nombre: str, apellidos: str, email: str, password: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s);"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            connection.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
    

    def identificar(self):
        pass