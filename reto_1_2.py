def es_palindromo(palabra):
    palabra = palabra.lower()
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[len(palabra) - 1 - i]:
            return print("No es palindromo")
    return print("Es palindromo")

palabra = str(input("Ingrese una plabra: "))
es_palindromo(palabra)