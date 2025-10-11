# dominio/usuario.py
# Esta clase representa a un usuario dentro del sistema SmartHome.
# Tiene atributos básicos como nombre, contraseña y rol.
# También puede tener métodos simples relacionados con su lógica, como validar si es administrador.

class Usuario:
    def __init__(self, id=None, nombre="", contrasena="", rol_id=2):
        # Por defecto, el rol 2 será "estándar" y el rol 1 será "admin".
        self.id = id
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol_id = rol_id

    def es_admin(self):
        """Devuelve True si el usuario tiene rol de administrador."""
        return self.rol_id == 1

    def mostrar_datos(self):
        """Devuelve un texto con los datos del usuario (para mostrar en consola)."""
        return f"ID: {self.id} | Nombre: {self.nombre} | Rol: {'Admin' if self.es_admin() else 'Estándar'}"

    def __str__(self):
        return self.mostrar_datos()
