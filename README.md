# Reto-1-POO
Reto 1 de Programación Orientada a Objetos

# Punto 1:
La solución define una función que toma una cadena como entrada, la cual contiene dos operandos y un operador separados por comas. Primero, se eliminan las comas con replace y se convierte la cadena en una lista de caracteres. Luego, se verifica la presencia del operador (+, -, *, /) en la lista y, según corresponda, realiza la operación básica utilizando los dos primeros elementos de la lista como operandos, convirtiéndolos en enteros con int. Finalmente, la función imprime el resultado.

# Punto 2:
La solución implementa una función para validar si una palabra es un palíndromo sin usar slicing. Primero, convierte la palabra a minúsculas para ignorar diferencias de mayúsculas y minúsculas. Luego, utiliza un bucle que itera hasta la mitad de la palabra, comparando el carácter en la posición actual con el carácter correspondiente desde el final (calculado como len(palabra) - 1 - i). Si algún par no coincide, se concluye que no es un palíndromo. Si el bucle termina sin encontrar diferencias, se confirma que la palabra es un palíndromo

# Punto 3:
La solución implementa una función que filtra los números primos de una lista. Primero, convierte la entrada en una lista de enteros y luego recorre cada número. Para cada número, verifica si es menor que 2 (descartándolo ya que no es primo). Después, utiliza un bucle que itera desde 2 hasta el número anterior al evaluado, comprobando si tiene divisores distintos de 1 y de sí mismo (usando el operador %). Si encuentra un divisor, interrumpe el bucle con break; si no encuentra divisores, agrega el número a la lista de primos usando un else emparejado con el bucle for. Finalmente, retorna e imprime la lista de números primos.

# Punto 4:
La solución implementa una función para encontrar la mayor suma entre dos números consecutivos en una lista. Primero, convierte la entrada en una lista de enteros. Luego, recorre los índices de la lista hasta el penúltimo elemento y calcula la suma de cada par de números consecutivos (lista_numeros[i] + lista_numeros[i+1]), almacenando los resultados en una lista auxiliar. Al final, utiliza la función max para encontrar el valor más alto en la lista de sumas y lo retorna como resultado.

# Punto 5:
La solución utiliza un diccionario para agrupar palabras que comparten los mismos caracteres. Para cada palabra en la lista, se calcula una clave ordenando alfabéticamente sus caracteres (por ejemplo, "amor" y "roma" se convierten en "amor"). Si esta clave ya existe en el diccionario, la palabra se agrega al grupo correspondiente; de lo contrario, se crea un nuevo grupo. Después, se recorren los valores del diccionario para identificar los grupos con más de una palabra (indicando que tienen los mismos caracteres). Estas palabras se añaden a una lista de resultados, que se imprime al final.
