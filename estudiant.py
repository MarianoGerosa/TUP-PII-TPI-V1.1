from usuario import Usuario
from curso import *
import funcionesListas as fl




class Estudiante(Usuario):
    def __init__(self, legajo:int, anioInscripcionCarrera:int, nombre, apellido, email, contrasenia) -> None:
        super().__init__(self,nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anioInscripcionCarrera
        self.__mis_cursos = []
    

    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def asiganarLegajo(self, legajo):
        self.__legajo = legajo

    @property
    def anio_inscripcion_carrera(self):
        return self.__anio_inscripcion_carrera
    
    @anio_inscripcion_carrera.setter
    def asiganarAnio_inscripcion_carrera(self, anio):
        self.__anio_inscripcion_carrera = anio

    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    @mis_cursos.setter
    def asiganarMis_cursos(self, curso):
        self.__mis_cursos = curso

    def __str__(self) -> str:
        return f"{self.__legajo} {self.__anio_inscripcion_carrera}"


    # def matricular_en_curso(self, opc):
    #     self.curso = curso

    def matricular_en_curso(self, opc):
            if opc in self.__mis_cursos:
                print("Usted ya está inscripto en este curso")
            else:
                contra = input("Ingrese la contraseña de matriculación: ")
                cursoElegido = fl.lista_cursos[opc]
            if contra == cursoElegido[1]:
                self.__mis_cursos.append(fl.lista_cursos[opc])
                print("Se ha añadido el curso a su lista de cursos")
                print(self.__mis_cursos)
            else:
                print("Contraseña incorrecta")

        # for i in self.__mis_cursos:
        #     if opc == self.__mis_cursos:
        #         print("Usted ya esta inscripto a este curso")               
        #     elif i == self.__mis_cursos[-1] and opc != self.__mis_cursos:
        #         contra = input("Ingrese la contraseña de matriculación: ")
        #         cursoElegido = fl.lista_cursos[opc]
        #         if contra == cursoElegido(1):
        #             self.__mis_cursos.append(fl.lista_cursos[opc])
        #             print("Se a añadido el curso a su lista de cursos")
        #             print(self.__mis_cursos)

    
    def verCursos(self):
        return self.__mis_cursos
                    

                    



