import psycopg2


def connect():
    return psycopg2.connect(user="postgres",password="99866",database="crud",host="localhost")
