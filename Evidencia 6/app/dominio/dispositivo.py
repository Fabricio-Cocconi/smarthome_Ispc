# dominio/dispositivo.py
# Esta clase representa a un dispositivo inteligente dentro del sistema SmartHome.
# Por ejemplo: una luz, una cámara, un sensor, etc.
# Aquí solo definimos sus datos y algunos métodos simples para cambiar su estado.

class Dispositivo:
    def __init__(self, id=None, nombre="", tipo="", estado=False, usuario_id=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado  # True = encendido / False = apagado
        self.usuario_id = usuario_id  # A qué usuario pertenece

    def encender(self):
        """Cambia el estado del dispositivo a encendido."""
        self.estado = True

    def apagar(self):
        """Cambia el estado del dispositivo a apagado."""
        self.estado = False

    def cambiar_estado(self):
        """Alterna el estado (si está encendido lo apaga y viceversa)."""
        self.estado = not self.estado

    def mostrar_info(self):
        """Devuelve un texto con la información del dispositivo."""
        estado_texto = "Encendido" if self.estado else "Apagado"
        return f"ID: {self.id} | Nombre: {self.nombre} | Tipo: {self.tipo} | Estado: {estado_texto}"

    def __str__(self):
        return self.mostrar_info()
