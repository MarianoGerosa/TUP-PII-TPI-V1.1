class curso():
    def __init__(self, nombre:str, contraMatri:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contraMatri

    def __str__(self) -> str:
        return f"{self.__nombre} {self.__contrasenia_matriculacion}"

    def generar_contrasenia_matriculacion(self):
        return