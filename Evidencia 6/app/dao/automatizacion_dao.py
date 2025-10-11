# dao/automatizacion_dao.py
# Esta clase maneja las operaciones sobre las automatizaciones en la base de datos.
# Implementa la interfaz IAutomatizacionDAO.

from conn.db_conn import DBConnection
from dao.interfaces.i_automatizacion_dao import IAutomatizacionDAO

class AutomatizacionDAO(IAutomatizacionDAO):
    def __init__(self, db_conn: DBConnection):
        self.db_conn = db_conn

    def crear(self, nombre, descripcion, usuario_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO automatizacion (nombre, descripcion, usuario_id) VALUES (%s, %s, %s)",
            (nombre, descripcion, usuario_id)
        )
        conn.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        return nuevo_id

    def obtener_por_id(self, automatizacion_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM automatizacion WHERE id = %s", (automatizacion_id,))
        registro = cursor.fetchone()
        cursor.close()
        return registro

    def listar_por_usuario(self, usuario_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM automatizacion WHERE usuario_id = %s", (usuario_id,))
        registros = cursor.fetchall()
        cursor.close()
        return registros

    def actualizar(self, automatizacion_id, nombre=None, descripcion=None):
        conn = self.db_conn.connect()
        cursor = conn.cursor()
        campos = []
        valores = []

        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)
        if descripcion:
            campos.append("descripcion = %s")
            valores.append(descripcion)

        if not campos:
            return 0

        sql = "UPDATE automatizacion SET " + ", ".join(campos) + " WHERE id = %s"
        valores.append(automatizacion_id)
        cursor.execute(sql, tuple(valores))
        conn.commit()
        afectados = cursor.rowcount
        cursor.close()
        return afectados

    def eliminar(self, automatizacion_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM automatizacion WHERE id = %s", (automatizacion_id,))
        conn.commit()
        eliminados = cursor.rowcount
        cursor.close()
        return eliminados
