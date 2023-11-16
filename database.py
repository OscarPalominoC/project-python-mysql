from decouple import config
import mysql.connector

HOST = config('HOST')
USER = config('USER')
PASSWORD = config('PASSWORD')
DATABASE = config('DATABASE')
PORT = config('PORT')

# Creating the connection to the database
def db_connection():
    """
    Create the connection to the database
    """
    connection = mysql.connector.connect(
        host = HOST,
        user = USER,
        passwd = PASSWORD,
        database = DATABASE,
        port = PORT
    )

    cursor = connection.cursor(buffered=True)

    return [connection, cursor]



