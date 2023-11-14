"""
Project Python and MySQL
- Open assisstant
- Login o register
- If we choose register, it will create an user in the DB
- If we choose login, identify the user and show the following menu:
    - Create note, show notes, delete note
"""

import database
from getpass import getpass
from utils import validate_email
from users.actions import Actions

print("""
Actions Available:
    - Register
    - Login
""")
Do = Actions()
action = input("What would you like to do? ")

if action.lower() == "register":
    print("Ok! Let's register us in the system...")
    Do.register()

elif action.lower() == "login":
    print("Ok! Let us login in the system...")
    Do.login()

else:
    print('That option is not available...')