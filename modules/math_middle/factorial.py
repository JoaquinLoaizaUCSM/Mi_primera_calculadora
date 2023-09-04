def factorial(n):
    """
    Retorna el factorial de n
    """
    if n == 0:
        print(f"El factorial de {n} es: 1")
        return 1
    elif n < 0:
        print(f"Error: El número debe ser mayor a cero")
        return 0
    else:
        print(f"El factorial de {n} es: {n} * factorial({n} - 1)")
        return n * factorial(n - 1)
