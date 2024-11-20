def mismos_caracteres(lista):
    agrupados = {}
    for palabra in lista:
        clave = "".join(sorted(palabra))
        if clave in agrupados:
            agrupados[clave].append(palabra)
        else:
            agrupados[clave] = [palabra]
    resultado = []
    for grupo in agrupados.values():
        if len(grupo) > 1:
            resultado.extend(grupo)
    return print(resultado)

mismos_caracteres(["amor", "roma", "perro", "maro", "arpa", "rapa"])