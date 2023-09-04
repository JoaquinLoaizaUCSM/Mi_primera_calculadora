from modules.math_basic import operations_basic
from modules.math_middle import comparaciones, factorial, mcd, mcm
from modules.math_advanced import fibonacci
from modules.check_data.verificar_datos import verificarNumero, ingreso_datos


def menu():
    print(
        """1. Operaciones básicas\n2. Comparisons\n3. Fibonacci\n4. Factorial\n5. mcm\n6. mcd\n"""
    )
    choice = input("Ingrese su opción: ")
    if choice == "1":
        menu_basicos()
    elif choice == "2":
        comparaciones.mayor_menor_igual(*ingreso_datos())
    elif choice == "3":
        fibonacci.fibonacci(verificarNumero("Ingrese el número: "))
    elif choice == "4":
        factorial.factorial(ingreso_datos())
    elif choice == "5":
        mcm.mcm(*ingreso_datos())
    elif choice == "6":
        mcd.mcd(*ingreso_datos())
    else:
        print("opción no válida")
        menu()


def menu_basicos():
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División con resto\n")
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
        print(operaciones_basicas.suma(*ingreso_datos()))
    elif opcion == "2":
        print(operaciones_basicas.resta(*ingreso_datos()))
    elif opcion == "3":
        print(operaciones_basicas.mutiplicacion(*ingreso_datos()))
    elif opcion == "4":
        print(operaciones_basicas.dividir(*ingreso_datos()))
    elif opcion == "5":
        print(operaciones_basicas.dividir_resto(*ingreso_datos()))
    else:
        print("Opción no válida")
        menu_basicos()
