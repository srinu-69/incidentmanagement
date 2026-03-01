# databaseconnection.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="db",  # Use the service name defined in docker-compose.yml
        user="pyuser",
        password="py123",
        database="pypro"
    )