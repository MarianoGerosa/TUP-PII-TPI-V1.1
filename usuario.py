from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, nombre, apellido, email, contrasenia) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def asignarNombre(self, nombre:str):
        self._nombre = nombre

    @property
    def apellido(self) -> str:
        return self._apellido
    
    @apellido.setter
    def asignarApellido(self, apellido:str):
        self._apellido = apellido

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def asignarEmail(self, email:str):
        self._email = email

    @property
    def contrasenia(self) -> str:
        return self._contrasenia
    
    @contrasenia.setter
    def asignarContrasenia(self, contrasenia:str):
        self._contrasenia = contrasenia
    
    def __str__(self) -> str:
        return f"{self._nombre} {self._apellido} {self._email} {self._contrasenia}"

    
    def validarEmailContasenia(self, email:str, contrasenia:str) -> bool:
        return (contrasenia == self._contrasenia and email == self._email)
    
    # @property
    # def validarEmailContasenia(self, email:str, contrasenia:str) -> bool:
    #     if (contrasenia == self._contrasenia and email == self._email):
    #         return True
    #     else:
    #         return False


