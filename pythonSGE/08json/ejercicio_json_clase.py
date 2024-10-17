'''
•	Crear una función que genere un fichero JSON con los mismos datos del ejercicio anterior (reutilizar código)
•	Crear una clase llamada Person que tenga un constructor que reciba como atributos los datos del fichero JSON (nombre, edad…)
•	Almacenar los atributos en variables de instancia dentro de la clase
•	Leer los datos del fichero JSON y convertirlos en un objeto de clase Person
•	Mostrar los atributos de la instancia de la clase 
•	Eliminar el fichero JSON 
'''

import os
import json

# Creación de diccionario
data = {
    "name": "prueba",
    "age": 34,
    "birth_date": "08-08-1987",
    "programming_languages":  ["Python", "Kotlin", "Swift"]
}

json_file = "prueba.json"

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data) 
        # json.dump convierte el diccionario en formato JSON y lo escribe en un archivo de texto

create_json()

# Crear una clase que almacena los datos del archivo JSON en __init__
class Data:
    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages


with open(json_file, "r") as json_data:   
    json_dict = json.load(json_data)
    # convierte los datos del fichero JSON en un diccionario

    # Conversión de JSON a clase: los datos se pasan al constructor de la clase Data
    # se crea un objeto que almacena los datos en forma de atributo
    json_class = Data(
        json_dict["name"],
        json_dict["age"],
        json_dict["birth_date"],
        json_dict["programming_languages"],
    )

    print(json_class.__dict__)
    # El atributo __dict__ contiene todas las variables de instancia de la clase

# os.remove(json_file)