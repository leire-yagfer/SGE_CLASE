"""
TÍTULO DEL PROGRAMA:
Este programa procesa una lista de parámetros y maneja varios tipos de excepciones, 
incluyendo una excepción personalizada para errores de tipo cadena.
"""

# definición de una clase de excepción personalizada llamada 'StrTypeError'
# se utiliza para manejar errores específicos cuando se encuentra un tipo de dato incorrecto (cadena de texto)
class StrTypeError(Exception):
    pass


# función que procesa una lista de parámetros
def process_params(parameters: list):
    
    # si la longitud de la lista de parámetros es menor que 3, lanza una excepción de tipo IndexError
    if len(parameters) < 3:
        raise IndexError()  # controla que la lista tenga al menos 3 elementos

    # si el segundo elemento de la lista (índice 1) es igual a 0, lanza una excepción ZeroDivisionError
    elif parameters[1] == 0:
        raise ZeroDivisionError()  # evita una división por cero más adelante

    # si el tercer elemento (índice 2) es de tipo cadena, lanza la excepción personalizada StrTypeError
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")  # asegura que el tercer elemento no sea una cadena
    
    # imprime el tercer elemento de la lista
    print(parameters[2])  # imprime el tercer valor de la lista

    # realiza una división entre el primer elemento (índice 0) y el segundo elemento (índice 1)
    print(parameters[0] / parameters[1])  # realiza una división entre los primeros dos elementos

    # intenta sumar 5 al tercer elemento
    print(parameters[2] + 5)  # suma 5 al tercer elemento (debe ser un número)


# bloque try-except para manejar diferentes tipos de excepciones
try:
    # se llama a la función process_params con una lista de 4 elementos
    process_params([23, 2, 2, 45])  # se pasan parámetros válidos a la función

# maneja la excepción IndexError cuando la lista tiene menos de 3 elementos
except IndexError as e:
    print("La lista debe tener más de 2 elementos")  # mensaje de error si la lista es demasiado corta

# maneja la excepción ZeroDivisionError cuando el segundo elemento es 0
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser cero")  # mensaje si el segundo valor es cero

# maneja la excepción personalizada StrTypeError cuando el tercer elemento es una cadena de texto
except StrTypeError as e:
    print(f"{e}")  # imprime el mensaje de la excepción si el tercer valor es una cadena

# maneja cualquier otra excepción inesperada
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")  # mensaje para cualquier error no controlado

# el bloque else se ejecuta si no se produjo ninguna excepción en el bloque try
else:
    print("No se ha producido ningún error")  # mensaje si no hubo errores

# el bloque finally siempre se ejecuta, ocurra o no una excepción
finally:
    print("El programa finaliza sin detenerse")  # mensaje final del programa

# mensaje que se imprime independientemente de los resultados del bloque try-except
print("Fin del programa")  # mensaje que indica el final del programa