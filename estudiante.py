from usuario import Usuario
from curso import *
import funcionesListas as fl

class Estudiante(Usuario):
    def __init__(self, legajo:int, anioInscripcionCarrera:int) -> None:
        super().__init__()
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anioInscripcionCarrera
        self.__mis_cursos = []

    def __str__(self) -> str:
        return f"{self.__legajo} {self.__anio_inscripcion_carrera}"
    

    
    def matricular_en_curso(self):
        self.curso = curso
        print("\n--- Lista de materias ---")
        print(f"1. Ingles I")
        print(f"2. Ingles II")
        print(f"3. Laboratorio I")
        print(f"4. Laboratorio II")
        print(f"5. Programación I")
        print(f"6. Programación II")

        opc = int(input("Ingrese una opcion: "))
        for i in self.__mis_cursos:
            if opc == self.__mis_cursos:
                print("Usted ya esta inscripto a este curso")               
            elif i == self.__mis_cursos[-1] and opc != self.__mis_cursos:
                contra = input("Ingrese la contraseña de matriculación: ")
                cursoElegido = fl.lista_cursos[opc]
                if contra == cursoElegido(1):
                    self.__mis_cursos.append(fl.lista_cursos[opc])
                    print("Se a añadido el curso a su lista de cursos")
                    print(self.__mis_cursos)


                
                    

                    



