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


#importo la biblioteca de peticiones
import requests

pokemon = input("Dime el nombre o número del POKEMON a buscar: ").lower() #paso lo que se introduzca a minúsculas

# La ayuda de la página nos da este ENDPOINT: https://pokeapi.co/api/v2/pokemon/{id or name}/

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")

if response.status_code == 200:
    print(response.text) #imprimo lo que guarda response

    data = response.json() #convierte el json en un diccionario

    #imprimo las características del pokemon elegido
    print("Nombre: ", data["name"])
    print("ID: ", data["id"])
    print("Peso: ", data["weight"])
    print("Altura: ", data["height"])
    print("Tipo(s): ")

    '''
    Cada elemento de data["types"] es un diccionario que tiene al menos una clave llamada "type", que a su vez es otro diccionario.
    El diccionario correspondiente a "type" contiene otra clave llamada "name", que almacena el nombre del tipo.
    '''
    for type in data["types"]: # types es una lista
        print(type["type"]["name"])

else:
    print(f"Error: {response.status_code}; el pokemon {pokemon} no se ha encontrado")