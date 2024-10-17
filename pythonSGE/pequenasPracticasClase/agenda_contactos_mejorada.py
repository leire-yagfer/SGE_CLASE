# PRÁCTICA 8

'''
Realizar lo mismo que en agenda_contactos.py, pero usando funciones para implementar todas las opciones de la agenda.
'''


def my_agenda():
    agenda = {}

    def insert_contact():
        while True:
            name = input("Introduce el nombre del contacto: ").strip()
            if name:
                break
            print("El nombre no puede estar vacío.")
        
        while True:
            phone = input("Introduce el teléfono del contacto (máximo 9 dígitos): ")
            if phone.isdigit() and 0 < len(phone) <= 9:
                agenda[name] = phone
                print(f"Contacto {name} insertado correctamente.")
                break
            else:
                print("Debes introducir un número de teléfono válido de máximo 9 dígitos.")

    def update_contact():
        name = input("Introduce el nombre del contacto a actualizar: ").strip()
        if name in agenda:
            insert_contact()
        else:
            print(f"El contacto {name} no existe.")

    def delete_contact():
        name = input("Introduce el nombre del contacto a eliminar: ").strip()
        if name in agenda:
            del agenda[name]
            print(f"Contacto {name} eliminado.")
        else:
            print(f"El contacto {name} no existe.")

    def search_contact():
        name = input("Introduce el nombre del contacto a buscar: ").strip()
        if name in agenda:
            print(f"El número de teléfono de {name} es {agenda[name]}.")
        else:
            print(f"El contacto {name} no existe.")

    def show_all_contacts():
        if agenda:
            print("\n--- Lista de todos los contactos ---")
            for name, phone in agenda.items():
                print(f"{name}: {phone}")
        else:
            print("La agenda está vacía.")

    while True:
        print("\n--- Menú de la agenda ---")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        
        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                search_contact()
            case "2":
                insert_contact()
            case "3":
                update_contact()
            case "4":
                delete_contact()
            case "5":
                show_all_contacts()
            case "6":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 6.")

my_agenda()
