from getpass import getpass
from utils import validate_email
from usuarios.usuario import Usuario as modelo

class Acciones:

    def registro(self):
        nombre = input("¿Cuál es tu nombre? ")
        apellidos = input("¿Cuál es tu apellido? ")
        email = input("¿Introduce tu email? ")
        password = getpass("Introduce tu contraseña? ")
        if validate_email(email):
            usuario = modelo(nombre, apellidos, email, password)
            registro = usuario.registrar()
            if registro[0] >= 1:
                print(f'te has registrado con el email {registro[1].email}')
            else:
                print('No te has registrado correctamente')
        else:
            print('Correo inválido')

    def login(self):
        email = input("¿Introduce tu email? ")
        password = getpass("Introduce tu contraseña? ")