class Usuario:
    def __init__(self, nombre, contrasena, rol="estandar"):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.nombre} | Rol: {self.rol}"

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, admin=False):
        nombre = input("Nombre de usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        rol = "admin" if admin else "estandar"
        usuario = Usuario(nombre, contrasena, rol)
        self.usuarios.append(usuario)
        print(f"Usuario '{nombre}' registrado como {rol}.")

    def iniciar_sesion(self):
        nombre = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contrasena == contrasena:
                print(f"Bienvenido, {usuario.nombre} ({usuario.rol})")
                return usuario
        print("Usuario o contraseña incorrectos.")
        return None

    def modificar_rol_usuario(self):
        nombre = input("Nombre del usuario a modificar: ").strip()
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                nuevo_rol = input("Nuevo rol (admin/estandar): ").strip().lower()
                if nuevo_rol in ["admin", "estandar"]:
                    usuario.rol = nuevo_rol
                    print(f"Rol de '{nombre}' cambiado a {nuevo_rol}.")
                else:
                    print("Rol no válido.")
                return
        print("Usuario no encontrado.")