# dao/dispositivo_dao.py
# Esta clase maneja todas las operaciones sobre los dispositivos:
# agregar, modificar, eliminar y consultar. 
# Es parte del patrón DAO y trabaja directamente con la base de datos.

from conn.db_conn import DBConnection
from dao.interfaces.i_dispositivo_dao import IDispositivoDAO

class DispositivoDAO(IDispositivoDAO):
    def __init__(self, db_conn: DBConnection):
        self.db_conn = db_conn

    def create(self, nombre, tipo, estado, usuario_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES (%s, %s, %s, %s)",
            (nombre, tipo, 1 if estado else 0, usuario_id)
        )
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return new_id

    def get_by_id(self, device_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM dispositivo WHERE id = %s", (device_id,))
        dispositivo = cursor.fetchone()
        cursor.close()
        return dispositivo

    def list_by_user(self, usuario_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM dispositivo WHERE usuario_id = %s", (usuario_id,))
        dispositivos = cursor.fetchall()
        cursor.close()
        return dispositivos

    def update(self, device_id, nombre=None, tipo=None, estado=None, usuario_id=None):
        conn = self.db_conn.connect()
        cursor = conn.cursor()
        campos = []
        valores = []

        if nombre is not None:
            campos.append("nombre = %s")
            valores.append(nombre)
        if tipo is not None:
            campos.append("tipo = %s")
            valores.append(tipo)
        if estado is not None:
            campos.append("estado = %s")
            valores.append(1 if estado else 0)
        if usuario_id is not None:
            campos.append("usuario_id = %s")
            valores.append(usuario_id)

        if not campos:
            return 0

        sql = "UPDATE dispositivo SET " + ", ".join(campos) + " WHERE id = %s"
        valores.append(device_id)
        cursor.execute(sql, tuple(valores))
        conn.commit()
        afectados = cursor.rowcount
        cursor.close()
        return afectados

    def delete(self, device_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dispositivo WHERE id = %s", (device_id,))
        conn.commit()
        eliminados = cursor.rowcount
        cursor.close()
        return eliminados
