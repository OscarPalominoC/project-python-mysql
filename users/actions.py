from getpass import getpass
from utils import validate_email
from users.user import User as model

class Actions:

    def register(self):
        name = input("What\'s your name? ")
        lastname = input("What\'s your lastname? ")
        email = input("What\'s your email? ")
        password = getpass("Type your password: ")
        if validate_email(email):
            user = model(name, lastname, email, password)
            register = user.register()
            if register[0] >= 1:
                print(f'You\'ve successfully registered with the email {register[1].email}.')
            else:
                print('You haven\'t registered successfully.')
        else:
            print('Invalid email.')

    def login(self):
        email = input("What\'s your email? ")
        password = getpass("Type your password: ")