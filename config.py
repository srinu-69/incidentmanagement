import mysql.connector
from mysql.connector import pooling
import os

db_pool = pooling.MySQLConnectionPool(
    pool_name="incident_pool",
    pool_size=5,
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"]
)

def get_db_connection():
    return db_pool.get_connection()