from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, legajo:int, anioInscripcionCarrera:int) -> None:
        super().__init__()
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anioInscripcionCarrera