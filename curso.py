import random
import string

class curso():
    def __init__(self, nombre:str, contrasenia_matriculacion:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.generar_contrasenia_matriculacion
        self.__carrera = "Tecnicatura Universitaria en Programacion"

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion


    def __str__(self) -> str:
        return f"{self.__nombre} {self.__contrasenia_matriculacion} {self.__carrera}"

    def generar_contrasenia_matriculacion(self):
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    
