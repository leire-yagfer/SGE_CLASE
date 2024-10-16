'''
•	Visitar la web: https://pokeapi.co y leer la documentación
•	En la pestaña “About”, leer la definición de API. Incluir un comentario con la definición en el fichero peticiones_api.py
•	Incluir otro comentario con la definición de API RESTful 
•	Incluir otro comentario con la definición de endpoint. Investigar cómo se usan los endpoints (pestaña API v2)
•	Ir a la pestaña API v2  menú izquierdo Pokémon  Pokemon ver el endpoint que sugieren. Escribirlo en un navegador y observar la respuesta (https://pokeapi.co/api/v2/pokemon/35/). Es un JSON con información del Pokemon 35: name, types, weight…

Después de revisar la documentación anterior, realiza un programa que haga lo siguiente:

•	Solicitar información de un Pokémon concreto, utilizando su nombre o número 

•	Controlar que el nombre del Pokémon esté en minúsculas

•	Mostrar los siguientes datos del Pokémon: nombre, id, peso, altura y tipos de Pokémon (esto es una lista)

•	Controlar errores
'''

import requests

pokemon = input("Dime el nombre o número del POKEMON a buscar: ").lower()

# La ayuda de la página nos da este ENDPOINT: https://pokeapi.co/api/v2/pokemon/{id or name}/

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    print(response.text)
    data = response.json() # convierte el json en un diccionario
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    print("Tipo(s): ")
    for type in data["types"]: # types es una lista
        print(type["type"]["name"])

else:
    print(f"Error: {response.status_code}; el pokemon {pokemon} no se ha encontrado")
