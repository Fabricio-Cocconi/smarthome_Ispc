class Dispositivo:
    def __init__(self, nombre, tipo, estado=False):
        self._nombre = nombre
        self._tipo = tipo
        self._estado = estado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    def cambiar_estado(self, encender=True):
        self._estado = encender

    def toggle(self):
        self._estado = not self._estado

    def __str__(self):
        estado_str = "Encendido" if self._estado else "Apagado"
        return f"{self._nombre} ({self._tipo}) - {estado_str}"
