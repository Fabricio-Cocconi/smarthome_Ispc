# conn/db_conn.py
# Esta clase se encarga de manejar la conexión con la base de datos MySQL.
# La usamos para abrir y cerrar la conexión cada vez que queremos leer o escribir datos.

import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self, host='localhost', user='root', password='', database='smarthome', port=3306):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '1234',
            'database': 'smarthome',
            'port': 3306
        }

        self.conn = None

    def connect(self):
        # Intenta conectarse a la base de datos.
        # Si ya hay una conexión abierta, la reutiliza.
        if self.conn and self.conn.is_connected():
            return self.conn
        try:
            self.conn = mysql.connector.connect(**self.config)
            return self.conn
        except Error as e:
            raise RuntimeError(f"No se pudo conectar a la base de datos: {e}")

    def close(self):
        # Cierra la conexión si está abierta.
        if self.conn and self.conn.is_connected():
            self.conn.close()
            self.conn = None
