from usuario import *
salir = False

alumnos_registrados = [Usuario("a", "a", "a", "a"), Usuario("b", "b", "b", "b")]

while salir == False:
    print("\n--- Menú ---")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    
    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        email = input("Ingrese su email: ")
        contrasenia = input("Ingrese su contraseña: ")
        #Usuario.validarEmailContasenia(email, contrasenia)
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    elif opc == 4:
        print("Hasta luego!")
        salir = True
    else:
        print("Opcion no valida")