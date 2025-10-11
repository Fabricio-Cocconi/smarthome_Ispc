# dao/interfaces/i_usuario_dao.py
# Esta interfaz define los métodos básicos que cualquier clase DAO de Usuario debe implementar.
# Es una guía para mantener una estructura ordenada en el acceso a datos.

from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):

    @abstractmethod
    def get_by_nombre(self, nombre):
        pass

    @abstractmethod
    def get_by_id(self, user_id):
        pass

    @abstractmethod
    def list_all(self):
        pass
