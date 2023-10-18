from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self) -> None:
        self._nombre = None
        self._apellido = None
        self._email = None
        self._contrasenia = None