import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "root"
}

connection = mysql.connector.connect(**config)

cursor = connection.cursor()