import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="studentuser",
        password="1234",
        database="student_db"
    )