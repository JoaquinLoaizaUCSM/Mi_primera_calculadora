def verificarNumero(numero):
    try:
        return round(float(numero))
    except ValueError:
        numero = input("Por favor ingresa un numero: ")
        return verificarNumero(numero)


def ingreso_datos():
    num1 = verificarNumero(input("Ingrese el primer número: "))
    num2 = verificarNumero(input("Ingrese el segundo número: "))
    return num1, num2
