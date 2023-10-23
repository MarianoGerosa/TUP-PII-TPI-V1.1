import os
from profesor import *

def subMenuProfesor (self):
    salir2 = False
    while salir2 == False:
        print("\n--- Sub Menú Profesor ---")
        print("1. Dictar curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")

        opc = int(input("\nIngrese una opcion: "))

        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 3:
            salir2 = True
            os.system('cls')
        else:
            print("Opcion no valida")