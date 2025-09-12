from .utilidades import mostrar_detalles_dispositivos

class Dispositivo:
    def __init__(self, nombre, tipo, estado=False):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    def cambiar_estado(self, encender=True):
        self.estado = encender

    def toggle(self):
        self.estado = not self.estado

    def __str__(self):
        estado_str = "Encendido" if self.estado else "Apagado"
        return f"{self.nombre} ({self.tipo}) - {estado_str}"

class GestorDispositivos:
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self, nombre, tipo):
        if tipo not in ["luz", "cafetera", "cámara"]:
            print("Tipo no válido.")
            return
        dispositivo = Dispositivo(nombre, tipo)
        self.dispositivos.append(dispositivo)
        print(f"Dispositivo '{nombre}' de tipo '{tipo}' agregado.")

    def listar_dispositivos(self):
        return self.dispositivos

    def buscar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == nombre:
                return dispositivo
        return None

    def eliminar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == nombre:
                self.dispositivos.remove(dispositivo)
                return f"Dispositivo '{nombre}' eliminado."
        return "Dispositivo no encontrado."

    def mostrar_detalles(self):
        mostrar_detalles_dispositivos(self.dispositivos)