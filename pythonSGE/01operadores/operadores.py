"""
Probar e indicar la utilidad de esta línea de código:
La siguiente línea de código evalúa el valor de la expresión {8 + 14}
y el resultado (22) se inserta dentro de la cadena, reemplazando dicha expresión.
"""
print(f"Suma: 8 + 14 = {8 + 14}")

"""
Voy a probar e indicar la utilidad de esta línea de código:
La siguiente línea evalúa el valor de la expresión {8 + 14}
y el resultado (22) se inserta en la cadena, reemplazando la expresión.
"""
print(f"Suma: 8 + 14 = {8 + 14}")

"""
Ejemplo sin f-string:
Concateno las cadenas y convierto el número a cadena.
"""
nombre = "Juan"
edad = 25
print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

"""
Ejemplo con f-string:
Utilizo una f-string para insertar las variables directamente en la cadena.
"""
nombre = "Juan"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años.")

"""
Ambos ejemplos imprimen el mismo resultado: Mi nombre es Juan y tengo 25 años.
"""


"""
Investigar cómo obtener texto escrito por teclado:
Para obtener datos del usuario, uso la función input(), que siempre devuelve una cadena.
Si necesito convertirlo a número, utilizo int() o float().
"""

# Obtengo texto por teclado
nombre = input("Introduce tu nombre: ")  # input me permite ingresar texto

# Muestro lo que introduje
print(f"Hola, {nombre}")



"""
Ejemplo de conversión:
Solicito un número por teclado y lo convierto a entero usando int().
"""

# Solicito una edad (número) por teclado
edad = int(input("Introduce tu edad: "))

# Muestro la edad introducida
print(f"Tienes {edad} años")



'''Indicar los operadores de comparación, lógicos y de asignación
a) Operadores de comparación:
    == : Igual a
    != : Distinto de
    > : Mayor que
    < : Menor que
    >= : Mayor o igual que
    <= : Menor o igual que
b) Operadores lógicos:
    and : Devuelve True si ambas condiciones son verdaderas.
    or : Devuelve True si al menos una de las condiciones es verdadera.
    not : Invierte el valor de la condición (si es True, lo convierte a False).
c) Operadores de asignación:
    = : Asignación simple.
    += : Suma y asigna (e.g., a += 5 es equivalente a a = a + 5).
    -= : Resta y asigna.
    *= : Multiplica y asigna.
    /= : Divide y asigna.
    %= : Asigna el resto de la división.'''