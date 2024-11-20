'''
Investigar qué son las funciones lambda, poniendo ejemplos
'''

'''
Las funciones lamba se usan para definir una función simple.
'''

#Sintaxis
'''lambda parámetros: expresión'''

# Función lambda con un parámetro
cuadrado = lambda x: x * x
print(cuadrado(5)) #le paso el 5 pq cuando haga la expresión lambda x = 5

# Función lambda con varios parámetros
suma = lambda x, y: x + y
print(suma(3,5)) #x=3 e y =5

# Filtrar una lista: lambda dentro de la función filter()
"""filter() filtra elementos de un iterable(lista, tupla...) que cumplan una condución
Sintaxis: filter(function, iterable).
Devuelve un objeto de tipo filter; hay que convertirlo a tipo iterable (lista...)
""" 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros)) # filter devuelve un objeto de tipo filter
print(pares)

# Mapear una lista: lambda dentro de la función map()
""" map() se usa para aplicar una función a cada uno de los elementos de un
iterable(lista, tupla...)
Sintaxis: map(function, iterable, ....).
Devuelve un objeto de tipo map; hay que convertirlo a tipo iterable (lista...)
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)




# --- MAS EJEMPLOS ---
#1. Defino una función lambda que suma dos números
suma = lambda a, b: a + b

# Uso la función lambda
resultado = suma(5, 3) # le paso dos número que son a y b 
print(f"La suma de 5 y 3 es: {resultado}")


#2. Utilizo una función lambda para ordenar una lista de tuplas por el segundo valor de cada tupla.
# Lista de tuplas
lista_tuplas = [(1, 5), (2, 3), (4, 1), (3, 2)]

# Ordeno la lista por el segundo valor de cada tupla usando lambda
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1]) #El parámetro key en la función sorted (y también en otras funciones como min o max) se utiliza para especificar una función que define el criterio de ordenación. 

# Imprimo la lista ordenada
print(f"Lista ordenada por el segundo valor de las tuplas: {lista_ordenada}")


#3. Filtrar los números pares de una lista.
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Uso de lambda con filter para obtener los números pares --> filtrar por la lamda
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimo los números pares
print(f"Números pares: {numeros_pares}")


#4. Elevar cada número de una lista al cuadrado.
# Lista de números
numeros = [1, 2, 3, 4, 5]

# Uso de lambda con map para elevar cada número al cuadrado --> aplicar la función, en este caso lambda, a cada elemento de la lista
cuadrados = list(map(lambda x: x ** 2, numeros))

# Imprimo los cuadrados
print(f"Cuadrados de los números: {cuadrados}")