class ReglaAutomatizacion:
    def __init__(self, condicion, accion, descripcion=""):
        self._condicion = condicion
        self._accion = accion
        self._descripcion = descripcion

    @property
    def condicion(self):
        return self._condicion

    @condicion.setter
    def condicion(self, value):
        self._condicion = value

    @property
    def accion(self):
        return self._accion

    @accion.setter
    def accion(self, value):
        self._accion = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    def evaluar(self):
        if self._condicion():
            self._accion()
            return True
        return False
