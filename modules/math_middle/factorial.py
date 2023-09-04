def factorial(n):
    """
    Retorna el factorial de n
    """
    if n == 0:
        print(f"El factorial de {n} es: 1")
        return 1
    else:
        print(f"El factorial de {n} es: {n} * factorial({n} - 1)")
        return n * factorial(n - 1)
