from usuario import *
import os

salir = False
alumnos_registrados = [Usuario("a", "a", "a", "a"), Usuario("b", "b", "b", "b")]
profesores_registrados = [Usuario("c", "c", "c", "c"), Usuario("d", "d", "d", "d")]

while salir == False:
    print("\n--- Menú ---")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    
    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        os.system('cls')
        email = input("Ingrese su email: ")
        contrasenia = input("Ingrese su contraseña: ")
        usuario_valido = None
        for usuario in alumnos_registrados:
            if usuario.validarEmailContasenia(email, contrasenia):
                usuario_valido = usuario
                break
        if usuario_valido:
            os.system('cls')
            print(f"Bienvenido, {usuario_valido.nombre}!")
            salir2 = False
            while salir2 == False:
                print("\n--- Sub Menú Alumno ---")
                print("1. Matricularse en un curso")
                print("2. Ver cursos")
                print("3. Volver al menú principal")

                opc = int(input("\Ingrese una opcion: "))

                if opc == 1:
                    pass
                elif opc == 2:
                    pass
                elif opc == 3:
                    salir2 = True
                    os.system('cls')
                else:
                    print("Opcion no valida")
        else:
            os.system('cls')
            print("Error de ingreso, verifique su email y contraseña.")

    elif opc == 2:
        email = input("Ingrese su email: ")
        contrasenia = input("Ingrese su contraseña: ")
        usuario_valido = None
        for usuario in profesores_registrados:
            if usuario.validarEmailContasenia(email, contrasenia):
                usuario_valido = usuario
                break
        if usuario_valido:
            os.system('cls')
            print(f"Bienvenido, {usuario_valido.nombre}!")
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
        else:
            os.system('cls')
            print("Error de ingreso, verifique su email y contraseña.")
    elif opc == 3:
        pass
    elif opc == 4:
        print("Hasta luego!")
        salir = True
    else:
        print("Opcion no valida")