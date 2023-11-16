from getpass import getpass
from utils import validate_email
from users.user import User as model
from notes.actions import Actions as NoteActions

class Actions:
    """
    Class for the User Actions
    """
    def register(self):
        """
        Register an user in the database.
        """
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
        """
        Verify if the user existis in the system.
        """
        try:
            email = input("What\'s your email? ")
            password = getpass("Type your password: ")

            user = model('', '', email, password)
            login = user.identify()

            if email == login[3]:
                print(f'Welcome {login[1]}, you\'ve registered in the system on {login[5]}')
                self.nextActions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print('Wrong login, please try again')
        finally:
            exit()

    def nextActions(self, user):
        """
        It creates the options the user has available after loging in.
        """
        print("""
Actions available:
- Create note (create)
- Show notes (show)
- Delete a note (delete)
- Exit (exit)
""")
        Do = NoteActions()
        action = input('What would you like to do? ')
        if action.lower() == 'create':
            print('Let\'s create a note ')
            Do.create(user)
            self.nextActions(user)
        elif action.lower() == 'show':
            print('User notes: ')
            Do.show(user)
            self.nextActions(user)
        elif action.lower() == 'delete':
            print('Let\'s delete a note')
            Do.delete(user)
            self.nextActions(user)
        elif action.lower() == 'exit':
            print('Goodbye')
            exit()
        else: 
            print('That action is not available')
        