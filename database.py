from decouple import config
import mysql.connector

HOST = config('HOST')
USER = config('USER')
PASSWORD = config('PASSWORD')
DATABASE = config('DATABASE')
PORT = config('PORT')

# Conectando a la base de datos
def db_connection():
    connection = mysql.connector.connect(
        host = HOST,
        user = USER,
        passwd = PASSWORD,
        database = DATABASE,
        port = PORT
    )

    return connection



