from usuario import Usuario
from curso import *

class Profesor(Usuario):
    def __init__(self, titulo:str, anioEgreso:int) -> None:
        super().__init__()
        self.__titulo = titulo
        self.__anio_egreso = anioEgreso

    def dictar_curso(self, curso:curso):
        self.curso = curso

    def __str__(self) -> str:
        return f"{self.__titulo} {self.__anio_egreso}"