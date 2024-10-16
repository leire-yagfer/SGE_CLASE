# PRÁCTICA 8

'''
•	Mostrar estas opciones: buscar contacto, insertar contacto, actualizar contacto, eliminar contacto, mostrar todos los contactos en orden ascendente y salir. Para esto es necesario crear un bucle del que sólo se saldrá cuando se seleccione la opción de salir.
•	Cada contacto debe contener un nombre y número de teléfono
•	Controlar que no se introduzcan números de teléfono no numéricos y que se introducen un máximo de 9 dígitos.
•	En primer lugar, el programa debe solicitar la operación a realizar, y a continuación los datos.
'''

def my_agenda():

# Lo más óptimo es usar un diccionario; clave: name y valor: teléfono
    agenda = {}

    def insert_contact():
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 9:
            agenda[name] = phone
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 9 dígitos.")
            
# Condición que siempre se cumple
    while True:

        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda: # Buscar por clave en un diccionario
                    print(
                        f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                if agenda:
                    agenda = dict(sorted(agenda.items()))
                    print(agenda)
                else:
                    print("La agenda está vacía")
            case "6":
                print("Saliendo de la agenda.")
                break # break sale del bucle donde se está ejecutando (while)
            case _:
                print("Opción no válida. Elige una opción del 1 al 6.")


my_agenda()
