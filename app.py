from usuario import *
from estudiant import *
import funcionesListas as fl  
import os
import subMenuAlumno as sma
import subMenuProfesor as smp


salir = False
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
        for usuario in fl.alumnos_registrados:
            if usuario.validarEmailContasenia(email, contrasenia):
                usuario_valido = usuario
                break
        if usuario_valido:
            os.system('cls')
            print(f"Bienvenido, {usuario_valido.nombre}!")
            sma.subMenuAlumnos()
        else:
            os.system('cls')
            print("Error de ingreso, verifique su email y contraseña.")
                
    elif opc == 2:
        os.system('cls')
        email = input("Ingrese su email: ")
        contrasenia = input("Ingrese su contraseña: ")
        usuario_valido = None
        for usuario in fl.profesores_registrados:
            if usuario.validarEmailContasenia(email, contrasenia):
                usuario_valido = usuario
                break
        if usuario_valido:
            os.system('cls')
            print(f"Bienvenido, {usuario_valido.nombre}!")
            smp.subMenuProfesor()
        else:
            os.system('cls')
            print("Error de ingreso, verifique su email y contraseña.")
            print("Para darse de alta, acercarse a alumnado")
    elif opc == 3:
        for curso in fl.listaCursosImprimir:
            print(f"Materia: {curso['Materia']}      Carrera: {curso['Carrera']}")


    elif opc == 4:
        print("Hasta luego!")
        salir = True
    else:
        print("Opcion no valida")