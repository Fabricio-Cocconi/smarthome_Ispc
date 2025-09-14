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