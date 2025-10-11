# dao/usuario_dao.py
# Esta clase se comunica con la base de datos para obtener o modificar información de los usuarios.
# No contiene lógica del negocio, solo acceso a datos (patrón DAO).

from conn.db_conn import DBConnection
from dao.interfaces.i_usuario_dao import IUsuarioDAO

class UsuarioDAO(IUsuarioDAO):
    def __init__(self, db_conn: DBConnection):
        self.db_conn = db_conn

    def get_by_nombre(self, nombre):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, contrasena, rol_id FROM usuario WHERE nombre = %s", (nombre,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def get_by_id(self, user_id):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, contrasena, rol_id FROM usuario WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def list_all(self):
        conn = self.db_conn.connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, rol_id FROM usuario")
        users = cursor.fetchall()
        cursor.close()
        return users
