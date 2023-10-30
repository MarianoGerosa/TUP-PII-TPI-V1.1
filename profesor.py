from usuario import Usuario
from curso import curso

class Profesor(Usuario):
    def __init__(self, titulo:str, anioEgreso:int, nombre, apellido, email, contrasenia ):
        super().__init__(self, nombre, apellido, email, contrasenia) 
        self.__titulo = titulo
        self.__anio_egreso = anioEgreso
        self.__mis_cursos = []

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def agregarTitulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    @anio_egreso.setter
    def agregarAnioEgreso(self, anioEgreso):
        self.__anio_egreso = anioEgreso

    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    @mis_cursos.setter
    def agregarMis_cursos(self, mis_cursos):
        self.__mis_cursos = mis_cursos

    def dictar_curso(self, curso:curso):
        self.curso = curso
        nombreCurso = input("Ingrese el nombre del nuevo curso: ")
        contraCurso = curso.generar_contrasenia_matriculacion(None)
        print(contraCurso)
        self.agregarMis_cursos.append(nombreCurso, contraCurso)
        print(self.mis_cursos)

    def __str__(self) -> str:
        return f"{self.__titulo} {self.__anio_egreso}"
    
   
        
profesores_registrados = [Usuario("c", "c", "c", "c"), Usuario("d", "d", "d", "d")]
