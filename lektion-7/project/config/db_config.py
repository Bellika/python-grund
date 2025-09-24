import mysql.connector

def get_conncection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='iot'
    )