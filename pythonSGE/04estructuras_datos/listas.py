'''
Investigar la estructura de datos llamada lista. 
Poner ejemplos de inserción, borrado, actualización y ordenación
'''

# Creación de una lista vacía
mi_lista = []

# Lista con elementos
mi_lista = [10, 20, 30, 40]

#INSERCIÓN 
mi_lista = [10, 20, 30]
mi_lista.append(40)  # Agrega el 40 al final
print(mi_lista)  # Salida: [10, 20, 30, 40]


#INSERCIÓN EN UNA POSICIÓN CONCRETA 
mi_lista = [10, 20, 30]
mi_lista.insert(1, 15)  # Inserta 15 en el índice 1
print(mi_lista)  # Salida: [10, 15, 20, 30]


#ELIMINAR 
mi_lista = [10, 20, 30, 40]
mi_lista.remove(20)  # Elimina el primer 20 que encuentra
print(mi_lista)  # Salida: [10, 30, 40]


#ELIMINAR DE UNA POSICIÓN CONCRETA
mi_lista = [10, 20, 30, 40]
mi_lista.pop(2)  # Elimina el elemento en la posición 2 (índice 2)
print(mi_lista)  # Salida: [10, 20, 40]


#ELIMINAR TODOS LOS ELEMENTOS
mi_lista = [10, 20, 30, 40]
mi_lista.clear()  # Elimina todos los elementos de la lista
print(mi_lista)  # Salida: []


#ACTUALIZACIÓN
mi_lista = [10, 20, 30, 40]
mi_lista[2] = 35  # Actualiza el valor en la posición 2
print(mi_lista)  # Salida: [10, 20, 35, 40]


#ORDENACIÓN ASCENDENTE
mi_lista = [40, 10, 30, 20]
mi_lista.sort()  # Ordena en orden ascendente
print(mi_lista)  # Salida: [10, 20, 30, 40]


#ORDENACIÓN DESCENDIENTE
mi_lista = [40, 10, 30, 20]
mi_lista.sort(reverse=True)  # Ordena en orden descendente
print(mi_lista)  # Salida: [40, 30, 20, 10]


#ORDENACIÓN SIN MODIFICAR LA ORIGINAL
mi_lista = [40, 10, 30, 20]
mi_lista_ordenada = sorted(mi_lista)  # Devuelve una nueva lista ordenada
print(mi_lista_ordenada)  # Salida: [10, 20, 30, 40]
print(mi_lista)  # La original no cambia: [40, 10, 30, 20]