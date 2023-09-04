def mayor_menor_igual(a, b):
    if a == b:
        print(f"{a} y {b} son iguales")
        return a, b
    elif a > b:
        print(f"{a} es mayor que {b}")
        return a
    elif a < b:
        print(f"{a} es menor que {b}")
        return b
