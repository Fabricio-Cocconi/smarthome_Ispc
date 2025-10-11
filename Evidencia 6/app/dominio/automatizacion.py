# dominio/automatizacion.py
# Esta clase representa una automatización dentro del sistema SmartHome.
# Una automatización define acciones automáticas que se activan cuando se cumplen ciertas condiciones.

class Automatizacion:
    def __init__(self, id=None, nombre="", descripcion="", usuario_id=None, reglas=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.usuario_id = usuario_id  # Usuario que la creó
        self.reglas = reglas if reglas is not None else []  # Lista de reglas asociadas

    def agregar_regla(self, regla):
        """Agrega una nueva regla a la automatización."""
        self.reglas.append(regla)

    def eliminar_regla(self, regla):
        """Elimina una regla existente."""
        if regla in self.reglas:
            self.reglas.remove(regla)

    def mostrar_info(self):
        """Devuelve una descripción legible de la automatización."""
        texto = f"ID: {self.id} | Nombre: {self.nombre} | Descripción: {self.descripcion}"
        if self.reglas:
            texto += f"\n  Reglas: {', '.join(self.reglas)}"
        else:
            texto += "\n  (Sin reglas definidas)"
        return texto

    def __str__(self):
        return self.mostrar_info()
