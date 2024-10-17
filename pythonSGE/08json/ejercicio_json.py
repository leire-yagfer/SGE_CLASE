'''
Incluir comentarios con información sobre los ficheros JSON: definición, elementos, características, usos principales…. 
'''
#JSON: Sirve para estructurar datos. Es una evolución de XML para los programadores. 

'''
Desarrollar un pequeño programa que cree un fichero JSON (con la sintaxis correcta) y guarde los siguientes datos:
o	Nombre (cadena de caracteres)
o	Edad (entero)
o	Fecha nacimiento (cadena de caracteres)
o	Módulos (lista de cadena de caracteres)
•	Mostrar el contenido del fichero y borrarlo
'''

import os
import json

# diccionario
data = {
    "name": "prueba",
    "age": 34,
    "birth_date": "08-08-1987",
    "programming_languages":  ["Python", "Kotlin", "Swift"]
}


json_file = "08json/prueba.json" #lugar donde se crea el fichero

#escritura
with open(json_file, "w") as json_data:
    json.dump(data, json_data) 
    # json.dump convierte el diccionario en formato JSON y lo escribe en un archivo de texto

#lectura por terminal
with open(json_file, "r") as json_data:
    print(json_data.read())

print("Borrando el fichero json por primera vez")
os.remove(json_file)