# dao/interfaces/i_automatizacion_dao.py
# Esta interfaz define los métodos que cualquier DAO de Automatización debe tener.
# Nos ayuda a mantener el código ordenado y modular.

from abc import ABC, abstractmethod

class IAutomatizacionDAO(ABC):

    @abstractmethod
    def crear(self, nombre, descripcion, usuario_id):
        pass

    @abstractmethod
    def obtener_por_id(self, automatizacion_id):
        pass

    @abstractmethod
    def listar_por_usuario(self, usuario_id):
        pass

    @abstractmethod
    def actualizar(self, automatizacion_id, nombre=None, descripcion=None):
        pass

    @abstractmethod
    def eliminar(self, automatizacion_id):
        pass
