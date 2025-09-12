from usuarios import usuarios

def cambiar_rol_usuario(admin_usuario):
    clave_ingresada = input("Ingrese su contraseña para confirmar cambios: ")
    if clave_ingresada != admin_usuario.password:
        print("Contraseña incorrecta. No se puede cambiar el rol.")
        return

    usuario_mod = input("Ingrese el nombre del usuario a modificar: ")
    for usuario in usuarios:
        if usuario.username == usuario_mod and usuario != admin_usuario:
            nuevo_rol = "admin" if usuario.role == "estándar" else "estándar"
            usuario.role = nuevo_rol
            print(f"Rol de '{usuario_mod}' cambiado a '{nuevo_rol}'")
            return

    print("Usuario no encontrado o no puede modificarse a sí mismo.")