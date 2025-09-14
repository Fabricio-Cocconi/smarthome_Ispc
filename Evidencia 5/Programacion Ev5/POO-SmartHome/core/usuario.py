class Usuario:
    def __init__(self, nombre, password, rol="user"):
        self._nombre = nombre
        self._password = password
        self._rol = rol

    @property
    def nombre(self):
        return self._nombre

    @property
    def rol(self):
        return self._rol

    def verificar_password(self, password):
        return self._password == password