from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, titulo:str, anioEgreso:int) -> None:
        super().__init__()
        self.__titulo = titulo
        self._anio_egreso = anioEgreso