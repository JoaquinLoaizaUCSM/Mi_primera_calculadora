def fibonacci(n):
    if n <= 0:
        print("Error: El número debe ser mayor a cero")
        return 0
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    print(f'El resultado de la serie fibonacci es: {" ".join(map(str, resultado))}')
    return resultado
