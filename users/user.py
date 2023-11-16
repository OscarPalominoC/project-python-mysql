from database import db_connection
from datetime import datetime
import hashlib

class User:
    """
    User class.

    Methods:
    - register: User registration in the DB.
    - Identify: Identify the user in the DB.
    """
    def __init__(self, name: str, lastname: str, email: str, password: str):
        """
        Constructor

        Args:
            name (str): User's name
            lastname (str): User's lastname
            email (str): User's email
            password (str): User's password
        """
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    def register(self):
        """
        Register the user in the DB.

        Returns:
            [Rows Produced, User]: List. It contains the rows affected and User object
        """
        connection, cursor = db_connection()
        fecha = datetime.now()

        # Encrypt password
        encrypted = hashlib.sha256()
        encrypted.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s);"
        user = (self.name, self.lastname, self.email, encrypted.hexdigest(), fecha)

        try:
            cursor.execute(sql, user)
            connection.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        finally:
            cursor.close()
            connection.close()

        return result
    

    def identify(self):
        """
        Identify the user in the database
        """
        connection, cursor = db_connection()
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        encrypted = hashlib.sha256()
        encrypted.update(self.password.encode('utf8'))

        # Information for query
        user = (self.email, encrypted.hexdigest())
        try:
            cursor.execute(sql, user)
            result = cursor.fetchone()
            
        except:
            print('Invalid email or password')
        finally:
            cursor.close()
            connection.close()

        return result