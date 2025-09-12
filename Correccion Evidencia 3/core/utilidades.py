# Esta función muestra todos los dispositivos registrados y su estado actual.
# Es útil para que el usuario vea qué dispositivos tiene y si están encendidos o apagados.
def mostrar_detalles_dispositivos(dispositivos):
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    print("\nLista de dispositivos registrados:")
    for dispositivo in dispositivos:
        # Mostramos el nombre, el tipo y si está encendido o apagado
        estado = "Encendido" if dispositivo.estado else "Apagado"
        print(f"- {dispositivo.nombre} ({dispositivo.tipo}) - {estado}")