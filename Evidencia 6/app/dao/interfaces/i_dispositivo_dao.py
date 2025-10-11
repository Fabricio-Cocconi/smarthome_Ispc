# dao/interfaces/i_dispositivo_dao.py
# Igual que la interfaz de Usuario, pero aplicada a los Dispositivos.
# Sirve para asegurarnos de que todas las clases DAO que creemos sigan la misma estructura.

from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):

    @abstractmethod
    def create(self, nombre, tipo, estado, usuario_id):
        pass

    @abstractmethod
    def get_by_id(self, device_id):
        pass

    @abstractmethod
    def list_by_user(self, usuario_id):
        pass

    @abstractmethod
    def update(self, device_id, nombre=None, tipo=None, estado=None, usuario_id=None):
        pass

    @abstractmethod
    def delete(self, device_id):
        pass
