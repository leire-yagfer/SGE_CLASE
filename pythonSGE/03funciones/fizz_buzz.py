'''
•	Crear una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
•	La función imprimirá todos los números del 1 al 100. Teniendo en cuenta que:
o	Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
o	Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
o	Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
•	La función retornará el número de veces que se ha impreso el número en lugar de los textos.
'''


def imprimir_numeros_y_cadenas(cadena1, cadena2):
    contador_numeros = 0  # Contador para los números impresos en lugar de textos
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:  # Múltiplo de 3 y 5
            print(cadena1 + cadena2)
        elif i % 3 == 0:  # Múltiplo de 3
            print(cadena1)
        elif i % 5 == 0:  # Múltiplo de 5
            print(cadena2)
        else:
            print(i)
            contador_numeros += 1  # Aumentar el contador cuando se imprime un número
    
    return contador_numeros

# Ejemplo de uso
cadena1 = "Fizz"
cadena2 = "Buzz"
resultado = imprimir_numeros_y_cadenas(cadena1, cadena2)
print(f"El número de veces que se imprimieron números fue: {resultado}")
