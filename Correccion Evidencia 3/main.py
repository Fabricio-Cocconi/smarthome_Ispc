from core.dispositivos import GestorDispositivos
from core.automatizacion import ReglaAutomatizacion
from core.usuarios import GestorUsuarios
from menu import mostrar_menu_estandar, mostrar_menu_admin

def main():
    gestor_dispositivos = GestorDispositivos()
    gestor_usuarios = GestorUsuarios()

    # Si no hay usuarios, registrar el primero como admin
    if not gestor_usuarios.usuarios:
        print("No hay usuarios registrados. Registre el primer usuario (será admin).")
        gestor_usuarios.registrar_usuario(admin=True)

    # Inicio de sesión
    usuario = gestor_usuarios.iniciar_sesion()
    if not usuario:
        print("Inicio de sesión fallido.")
        return

    # Automatización predefinida
    def condicion():
        return any(d.tipo.lower() == "luz" for d in gestor_dispositivos.dispositivos)

    def accion():
        for dispositivo in gestor_dispositivos.dispositivos:
            if dispositivo.tipo.lower() == "luz":
                dispositivo.toggle()

    regla = ReglaAutomatizacion(condicion, accion, "Alternar luces encendidas/apagadas")

    # Menú según rol
    if usuario.rol == "admin":
        mostrar_menu_admin(gestor_dispositivos, gestor_usuarios, regla)
    else:
        mostrar_menu_estandar(usuario, gestor_dispositivos, regla)

if __name__ == "__main__":
    main()