def mcm(num1, num2):
    """
    La función mcm() calcula el mínimo común múltiplo de dos números.
    """
    # Se elige el mayor de los dos números
    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            mcm = greater
            break
        greater += 1
    print(f"El mcm de {num1} y {num2} es {mcm}")
    return mcm
