def suma(num1, num2):
    print(f"La suma de {num1} y {num2} es {num1 + num2}")
    return num1 + num2


def resta(num1, num2):
    print(f"La resta de {num1} y {num2} es {num1 - num2}")
    return num1 - num2


def mutiplicacion(num1, num2):
    print(f"La multiplicación de {num1} y {num2} es {num1 * num2}")
    return round(num1 * num2,2)


def dividir(num1, num2):
    if num2 == 0:
        print("Error: No se puede dividir por cero")
        return 0
    else:
        print(f"La división de {num1} y {num2} es {num1 / num2}")
        return round(num1 / num2,2)


def dividir_resto(num1, num2):
    if num2 == 0:
        print("Error: No se puede dividir por cero")
        return 0
    else:
        print(f"El resto de la división de {num1} y {num2} es {num1 % num2}")
        return num1 % num2
