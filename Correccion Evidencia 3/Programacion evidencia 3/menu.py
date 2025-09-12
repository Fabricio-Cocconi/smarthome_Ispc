from core.utilidades import mostrar_detalles_dispositivos

def mostrar_menu_estandar(usuario, gestor_dispositivos, regla):
    while True:
        print("\n=== MENÚ USUARIO ESTÁNDAR ===")
        print("1. Consultar datos personales")
        print("2. Ejecutar automatización")
        print("3. Consultar dispositivos")
        print("0. Cerrar sesión")
        print("9. Salir del sistema")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            print(f"\nUsuario: {usuario.nombre}\nRol: {usuario.rol}")
        elif opcion == "2":
            regla.evaluar()
        elif opcion == "3":
            dispositivos = gestor_dispositivos.listar_dispositivos()
            mostrar_detalles_dispositivos(dispositivos)
        elif opcion == "0":
            print("Cerrando sesión...")
            return False  # Volver al login
        elif opcion == "9":
            return True   # Salir del sistema
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

def mostrar_menu_admin(gestor_dispositivos, gestor_usuarios, regla):
    while True:
        print("\n=== MENÚ ADMIN ===")
        print("1. Consultar automatización activa")
        print("2. Gestionar dispositivos")
        print("3. Modificar rol de usuario")
        print("4. Registrar nuevo usuario")
        print("0. Cerrar sesión")
        print("9. Salir del sistema")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            print(f"Automatización activa: {regla.descripcion}")
        elif opcion == "2":
            mostrar_menu_gestion_dispositivos(gestor_dispositivos)
        elif opcion == "3":
            gestor_usuarios.modificar_rol_usuario()
        elif opcion == "4":
            gestor_usuarios.registrar_usuario(admin=False)
        elif opcion == "0":
            print("Cerrando sesión...")
            return False  # Volver al login
        elif opcion == "9":
            return True   # Salir del sistema
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

def mostrar_menu_gestion_dispositivos(gestor):
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("0. Volver")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            nombre = input("Nombre del dispositivo: ").strip()
            tipo = input("Tipo (luz, cafetera, cámara): ").strip().lower()
            gestor.agregar_dispositivo(nombre, tipo)
        elif opcion == "2":
            dispositivos = gestor.listar_dispositivos()
            mostrar_detalles_dispositivos(dispositivos)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            dispositivo = gestor.buscar_dispositivo(nombre)
            print(dispositivo if dispositivo else "❌ Dispositivo no encontrado.")
        elif opcion == "4":
            nombre = input("Nombre del dispositivo a eliminar: ").strip()
            print(gestor.eliminar_dispositivo(nombre))
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")