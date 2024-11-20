def suma_mayor(lista_numeros):
    lista_sumas = []
    lista_numeros = list(lista_numeros)
    for i in range(0, len(lista_numeros)-1):
        suma = int(lista_numeros[i]) + int(lista_numeros[i+1])
        lista_sumas.append(suma)
    return print(f"La suma de numeros consecutivos más grandes es: {max(lista_sumas)}")

lista_numeros = str(input("Ingrese más de 2 números para sumar: "))
suma_mayor(lista_numeros)