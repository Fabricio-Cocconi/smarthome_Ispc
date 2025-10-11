# Este archivo es el punto de entrada del sistema SmartHome
# Se encarga de manejar el inicio de sesion y los menus de opciones
# El objetivo es ofrecer una experiencia simple y clara para el usuario

from conn.db_conn import DBConnection
from dao.usuario_dao import UsuarioDAO
from dao.dispositivo_dao import DispositivoDAO
from dao.automatizacion_dao import AutomatizacionDAO

# Funcion para separar visualmente las secciones del menu
def separador():
    print("\n" + "=" * 60 + "\n")

# Funcion para mostrar un titulo centrado
def cabecera(texto):
    print("=" * 60)
    print(texto.center(60))
    print("=" * 60)

# ---------------------------------------------------------
# Menu para los usuarios comunes
# ---------------------------------------------------------
def menu_estandar(usuario, dispositivo_dao, automatizacion_dao):
    while True:
        separador()
        cabecera(f"Bienvenido {usuario['nombre']} al panel de SmartHome")
        print("Estas en tu menu personal de usuario")
        print("Aqui podes ver tus datos y dispositivos\n")

        print("1. Ver mis datos personales")
        print("2. Ver mis dispositivos")
        print("3. Ver mis automatizaciones")
        print("0. Cerrar sesion")
        opcion = input("\nElige una opcion: ")

        if opcion == "1":
            separador()
            print("Tus datos personales:")
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            rol = "Administrador" if usuario["rol_id"] == 1 else "Estandar"
            print(f"Rol: {rol}")
            input("\nPresiona Enter para volver al menu...")
        elif opcion == "2":
            separador()
            dispositivos = dispositivo_dao.list_by_user(usuario["id"])
            if not dispositivos:
                print("No tenes dispositivos registrados todavia")
            else:
                print("Tus dispositivos:")
                for d in dispositivos:
                    estado = "Encendido" if d["estado"] else "Apagado"
                    print(f" - {d['nombre']} ({d['tipo']}) [{estado}]")
            input("\nPresiona Enter para volver al menu...")
        elif opcion == "3":
            separador()
            autos = automatizacion_dao.listar_por_usuario(usuario["id"])
            if not autos:
                print("No tenes automatizaciones configuradas por ahora")
            else:
                print("Tus automatizaciones:")
                for a in autos:
                    print(f" - {a['nombre']} ({a['descripcion']})")
            input("\nPresiona Enter para volver al menu...")
        elif opcion == "0":
            print("\nCerrando sesion...")
            break
        else:
            print("Opcion no valida, intenta de nuevo")

# ---------------------------------------------------------
# Menu para los administradores
# ---------------------------------------------------------
def menu_admin(usuario, usuario_dao, dispositivo_dao, automatizacion_dao):
    while True:
        separador()
        cabecera(f"Panel de Administrador - {usuario['nombre']}")
        print("Hola admin, desde aqui podes gestionar usuarios y dispositivos\n")
        print("1. Ver todos los usuarios")
        print("2. Gestionar dispositivos")
        print("3. Ver automatizaciones registradas")
        print("0. Cerrar sesion")
        opcion = input("\nElige una opcion: ")

        if opcion == "1":
            separador()
            print("Lista de usuarios registrados en el sistema:\n")
            usuarios = usuario_dao.list_all()
            for u in usuarios:
                rol = "Admin" if u["rol_id"] == 1 else "Estandar"
                print(f"ID: {u['id']} | Nombre: {u['nombre']} | Rol: {rol}")
            input("\nPresiona Enter para volver al menu...")
        elif opcion == "2":
            separador()
            print("Gestion de dispositivos")
            print("1. Crear nuevo dispositivo")
            print("2. Modificar dispositivo existente")
            print("3. Eliminar dispositivo")
            print("0. Volver atras")
            sub = input("\nElige una opcion: ")

            if sub == "1":
                nombre = input("Nombre del dispositivo: ")
                tipo = input("Tipo de dispositivo: ")
                estado = input("Encendido (1=si, 0=no): ") == "1"
                usuario_id = input("ID del usuario propietario: ")
                nuevo_id = dispositivo_dao.create(nombre, tipo, estado, usuario_id)
                print(f"\nDispositivo creado correctamente con ID {nuevo_id}")
            elif sub == "2":
                id_disp = input("ID del dispositivo a modificar: ")
                nombre = input("Nuevo nombre (deja vacio para no cambiar): ") or None
                tipo = input("Nuevo tipo (deja vacio para no cambiar): ") or None
                estado = input("Nuevo estado (1=on, 0=off o vacio): ")
                estado = True if estado == "1" else False if estado == "0" else None
                filas = dispositivo_dao.update(id_disp, nombre, tipo, estado)
                print("Dispositivo actualizado" if filas else "No se realizaron cambios")
            elif sub == "3":
                id_disp = input("ID del dispositivo a eliminar: ")
                filas = dispositivo_dao.delete(id_disp)
                print("Dispositivo eliminado" if filas else "No se encontro el dispositivo")
            elif sub == "0":
                continue
            else:
                print("Opcion no valida")
            input("\nPresiona Enter para volver al menu principal...")
        elif opcion == "3":
            separador()
            print("Automatizaciones registradas:\n")
            autos = automatizacion_dao.listar_por_usuario(usuario["id"])
            if not autos:
                print("No hay automatizaciones cargadas")
            else:
                for a in autos:
                    print(f"{a['id']} - {a['nombre']} ({a['descripcion']})")
            input("\nPresiona Enter para continuar...")
        elif opcion == "0":
            print("\nCerrando sesion...")
            break
        else:
            print("Opcion no valida")

# ---------------------------------------------------------
# Funcion para iniciar sesion
# ---------------------------------------------------------
def login(usuario_dao):
    while True:
        separador()
        cabecera("Bienvenido al sistema SmartHome")
        print("Por favor inicia sesion con tu nombre de usuario y contrasena\n")
        nombre = input("Usuario: ").strip()
        contrasena = input("Contrasena: ").strip()

        user = usuario_dao.get_by_nombre(nombre)
        if not user:
            print("\nNo existe un usuario con ese nombre")
        elif user["contrasena"] != contrasena:
            print("\nLa contrasena ingresada no es correcta")
        else:
            print(f"\nBienvenido {user['nombre']} al sistema SmartHome")
            return user

        if input("\nIntentar otra vez (s/n): ").lower() != "s":
            return None

# ---------------------------------------------------------
# Programa principal
# ---------------------------------------------------------
def main():
    cabecera("INICIANDO PROGRAMA SMART HOME")

    # Se conecta a la base de datos
    db = DBConnection(host="localhost", user="root", password="1234", database="smarthome")
    db.connect()

    # Se crean los objetos DAO para manejar los datos
    usuario_dao = UsuarioDAO(db)
    dispositivo_dao = DispositivoDAO(db)
    automatizacion_dao = AutomatizacionDAO(db)

    # Bucle principal del programa
    while True:
        usuario = login(usuario_dao)
        if not usuario:
            break

        if usuario["rol_id"] == 1:
            menu_admin(usuario, usuario_dao, dispositivo_dao, automatizacion_dao)
        else:
            menu_estandar(usuario, dispositivo_dao, automatizacion_dao)

        if input("\nDeseas salir del programa (s/n): ").lower() == "s":
            break

    db.close()
    print("\nGracias por usar SmartHome, hasta la proxima")

if __name__ == "__main__":
    main()
