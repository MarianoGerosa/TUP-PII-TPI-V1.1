import os
from estudiante import *

def subMenuAlumnos(self) -> str:
    salir2 = False
    while salir2 == False:
        print("\n--- Sub Menú Alumno ---")
        print("1. Matricularse en un curso")
        print("2. Ver cursos")
        print("3. Volver al menú principal")

        opc = int(input("Ingrese una opcion: "))

        if opc == 1:
            os.system('cls')
            print("\n--- Lista de materias ---")
            print(f"1. Ingles I")
            print(f"2. Ingles II")
            print(f"3. Laboratorio I")
            print(f"4. Laboratorio II")
            print(f"5. Programación I")
            print(f"6. Programación II")

            opc = int(input("Ingrese una opcion: "))
            # estudiante = Estudiante()
            # estudiante.matricular_en_curso(opc)
            # Estudiante.matricular_en_curso(opc)
        elif opc == 2:
            Estudiante.verCursos()
        elif opc == 3:
            salir2 = True
            os.system('cls')
        else:
            print("Opcion no valida")
