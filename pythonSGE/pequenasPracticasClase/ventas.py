# PRÁCTICA 9

'''
•	Crear un programa almacenará los datos de productos de una empresa en un fichero llamado ventas.txt
•	Realizar un menú que muestre por terminal las siguientes opciones:
1.	Añadir producto
2.	Consultar producto
3.	Actualizar producto
4.	Borrar producto
5.	Mostrar todos los productos
6.	Calcular venta total
7.	Calcular venta por producto
8.	Salir
•	En cada línea del fichero se tiene que guardar la siguiente información de cada producto: nombre, cantidad, precio.
•	La opción de “Salir” debe salir del programa y borrar el fichero ventas.txt
'''

# Control de gestión de inventario

import os

file_name = "ventas.txt"

"""Inicializar el fichero antes de usar el programa para evitar 
error al tratar de eliminar (opción 8),
para añadir datos en el fichero: poner la opción a (w sobreescribe datos)"""

open(file_name, "a")

# Bucle infinito para preguntar al usuario qué quiere hacer:
while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar todos los productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "a") as file:
            file.write(f"{name}, {quantity}, {price}\n")

    elif option == "2":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break

    elif option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file: # La opción w borra el contenido del fichero
            for line in lines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)
    elif option == "4":
        name = input("Nombre: ")
        with open(file_name, "r") as file:
            lines = file.readlines()
        with open(file_name, "w") as file:
            for line in lines:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif option == "5":
        with open(file_name, "r") as file:
            print(file.read())

    elif option == "6":
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
        
    elif option == "7":
        name = input("Nombre: ")
        total = 0
        with open(file_name, "r") as file:
            for line in file.readlines():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
                    break
        print(total)

    elif option == "8":
        # os.remove(file_name)
        break
    else:
        print("Selecciona una opción disponible")


