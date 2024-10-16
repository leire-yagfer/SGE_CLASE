'''
Investigar la estructura if y crear un ejemplo. Hacer print por consola del resultado
'''
#Estructura if
'''
if condición:
    # Código que se ejecuta si la condición es verdadera
elif otra_condición:
    # Código que se ejecuta si la otra condición es verdadera
else:
    # Código que se ejecuta si ninguna condición anterior es verdadera
'''

#Ejemplo if: Pido la edad del usuario y determino si es menor de edad, mayor de edad o adulto mayor. El resultado dependerá de la edad introducida por el usuario
# Pido la edad al usuario
edad = int(input("Introduce tu edad: "))

# Evaluo la edad usando la estructura if
if edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres mayor de edad.")
else:
    print("Eres adulto mayor.")




'''
Investigar la estructura case y crear un ejemplo. Hacer print por consola del resultado
'''
#Estructura case
'''
match variable:
    case valor1:
        # Código a ejecutar si variable == valor1
    case valor2:
        # Código a ejecutar si variable == valor2
    case _:
        # Código a ejecutar si ninguna de las condiciones anteriores se cumple
'''

# Ejemplo match-case:  Determino si el día introducido es laborable o es fin de semana. El resultado se imprimirá en la consola según el día introducido por el usuario
# Pido un día de la semana al usuario
dia_semana = input("Introduce un día de la semana (en minúsculas): ")

# Uso match-case para decidir qué mensaje mostrar
match dia_semana:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print(f"{dia_semana.capitalize()} es un día laborable.")
    case "sábado" | "domingo":
        print(f"{dia_semana.capitalize()} es fin de semana.")
    case _:
        print("El día introducido no es válido.")