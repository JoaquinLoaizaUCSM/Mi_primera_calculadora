def mcd(a, b):
    """
    Retorna el maximo comun divisor de a y b
    """
    while b:
        a, b = b, a % b

    print(f"El maximo comun divisor de {a} y {b} es: {a}")
    return a
