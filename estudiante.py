from usuario import Usuario
from curso import *

class Estudiante(Usuario):
    def __init__(self, legajo:int, anioInscripcionCarrera:int) -> None:
        super().__init__()
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anioInscripcionCarrera

    def __str__(self) -> str:
        return f"{self.__legajo} {self.__anio_inscripcion_carrera}"
    
    def matricular_en_curso(self, curso:curso):
        self.curso = curso

