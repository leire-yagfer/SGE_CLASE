'''
Investigar la estructura de datos llamada set. 
Poner ejemplos de inserción, borrado, actualización y ordenación
'''


'''
Mutable: Puedes agregar o eliminar elementos, pero no puedes acceder a elementos por índice ya que no están ordenados.
No ordenados: No mantienen ningún orden particular de los elementos.
No permiten duplicados: Todos los elementos en un set deben ser únicos.
Sintaxis: Se definen usando llaves {} o la función set().
'''

# creación de un set vacío
mi_set = set()

# set con elementos
mi_set = {10, 20, 30, 40}


#INSERCIÓN
# agregando un nuevo elemento
mi_set.add(40)  # ahora el set es {10, 20, 30, 40}

# intentando agregar un duplicado
mi_set.add(20)  # no cambia nada porque 20 ya está en el set
print(mi_set)  # salida: {10, 20, 30, 40}


#BORRADO
# eliminando un elemento con remove
mi_set.remove(30)  # ahora es {10, 20, 40}

# eliminando un elemento con discard (no da error si el elemento no existe)
mi_set.discard(50)  # no pasa nada porque 50 no está en el set

# usando pop para eliminar un elemento aleatorio
mi_set.pop()  # elimina un elemento aleatorio, por ejemplo, 10

# vaciando el set con clear
mi_set.clear()  # el set ahora está vacío


#ACTUALIZACIÓN
# actualizando el set con nuevos elementos desde una lista
mi_set.update([40, 50])

# también puedes usar otro set
mi_set.update({60, 70})

print(mi_set)  # salida: {10, 20, 30, 40, 50, 60, 70}


#ORDENACIÓN
# convirtiendo el set en una lista para ordenarla
lista_ordenada = sorted(mi_set)

print(lista_ordenada)  # salida: [10, 20, 30, 40]