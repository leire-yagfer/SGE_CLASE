'''
Investigar la estructura de datos llamada tupla. 
Poner ejemplos de inserción, borrado, actualización y ordenación
'''


'''
Inmutables: Una vez creada, no puedes modificar, agregar o eliminar elementos.
Ordenadas: Mantienen el orden de los elementos.
Permiten duplicados: Al igual que las listas, puedes tener elementos repetidos.
Sintaxis: Se definen usando paréntesis ().
'''


# Creación de una tupla vacía
mi_tupla = ()

# Tupla con elementos
mi_tupla = (10, 20, 30, 40)

# También se puede crear sin paréntesis
mi_tupla = 10, 20, 30, 40

# inserción en una tupla
# las tuplas son inmutables, por lo que no se pueden modificar directamente. para agregar elementos, hay que crear una nueva tupla
mi_tupla = mi_tupla + (50,)  # concatenación de una nueva tupla con el valor 50

# borrado en una tupla
# no se pueden eliminar elementos de una tupla directamente, pero se puede crear una nueva sin el elemento que se quiere eliminar
mi_tupla = mi_tupla[:2] + mi_tupla[3:]  #mi_tupla[:2]: selecciona desde el inicio hasta el índice 2 (no incluido), lo que da (10, 20). mi_tupla[3:]: selecciona desde el índice 3 hasta el final, lo que da (40,).

# actualización de una tupla
# como las tuplas son inmutables, para "actualizar" un elemento, hay que crear una nueva tupla con el cambio deseado
mi_tupla = mi_tupla[:1] + (15,) + mi_tupla[2:]  # cambiando el segundo valor (índice 1)

# ordenación de una tupla
# no se puede ordenar una tupla directamente, pero se puede convertir en una lista, ordenarla y luego volver a convertirla en tupla
mi_tupla_ordenada = tuple(sorted(mi_tupla))

# resultado final
print("Tupla original:", mi_tupla)
print("Tupla ordenada:", mi_tupla_ordenada)