def operaciones_basicas(operacion ):
    cadena = operacion.replace(",","")
    cadena = list(cadena)
    if "+" in cadena:
        print(int(cadena[0]) + int(cadena[1]))
    elif "-" in cadena:
        print(int(cadena[0]) - int(cadena[1]))
    elif "*" in cadena:
        print(int(cadena[0]) * int(cadena[1]))
    elif "/" in cadena:
        print(int(cadena[0]) / int(cadena[1]))

operacion = str(input("Ingrese una operación de 2 números y el signo separados por una coma: "))
operaciones_basicas(operacion)
