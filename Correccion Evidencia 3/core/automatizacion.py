class ReglaAutomatizacion:
    def __init__(self, condicion, accion, descripcion=""):
        self.condicion = condicion
        self.accion = accion
        self.descripcion = descripcion

    def evaluar(self):
        if self.condicion():
            self.accion()
            print(f"Regla ejecutada: {self.descripcion}")
        else:
            print("Condición no cumplida. No se ejecuta la automatización.")

def alternar_luces(gestor):
    luces = [d for d in gestor.dispositivos if d.tipo == "luz"]
    if not luces:
        print("No se encuentran luces disponibles para automatización.")
        return

    luces_encendidas = all(luz.estado for luz in luces)

    if luces_encendidas:
        print("\nApagando luces:")
        for luz in luces:
            luz.estado = False
            print(f"{luz.nombre} - Apagado")
    else:
        print("\nEncendiendo luces:")
        for luz in luces:
            luz.estado = True
            print(f"{luz.nombre} - Encendido")

def modo_desayuno(gestor):
    luces_cocina = [d for d in gestor.dispositivos if d.tipo == "luz" and "cocina" in d.nombre.lower()]
    cafeteras = [d for d in gestor.dispositivos if d.tipo == "cafetera"]

    if not luces_cocina and not cafeteras:
        print("No hay luces de cocina ni cafetera registradas.")
        return

    for luz in luces_cocina:
        luz.estado = True
        print(f"Luz '{luz.nombre}' - Encendida")

    for cafetera in cafeteras:
        cafetera.estado = True
        print(f"Cafetera '{cafetera.nombre}' - Encendida")

    print("¡Modo desayuno activado!")