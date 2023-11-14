"""
Proyecto Python y MySQL
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la DB
- Si elegimos login, identifica al usuario y muestra el siguiente menú:
    - Crear nota, mostrar nota, borrar nota
"""

import database
from getpass import getpass
from utils import validate_email
from usuarios.acciones import Acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")
hazEl = Acciones()
accion = input("¿Qué quieres hacer? ")

if accion.lower() == "registro":
    print("Ok! Vamos a registrarte en el sistema...")
    hazEl.registro()

elif accion.lower() == "login":
    print("Ok! Vamos a iniciar sesión en el sistema...")
    hazEl.login()

else:
    print('Esa acción no está disponible...')