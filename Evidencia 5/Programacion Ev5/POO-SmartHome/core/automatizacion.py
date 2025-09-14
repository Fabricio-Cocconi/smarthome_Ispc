class ReglaAutomatizacion:
    def __init__(self, condicion, accion, descripcion=""):
        self.condicion = condicion
        self.accion = accion
        self.descripcion = descripcion

    def evaluar(self):
        if self.condicion():
            self.accion()
            return True
        return False