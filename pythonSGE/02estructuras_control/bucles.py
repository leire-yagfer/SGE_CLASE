'''
Investigar la estructura iterativa for y crear un ejemplo. Hacer print por consola del resultado
'''
# Estructura for
'''
for variable in secuencia:
    Código que se ejecuta para cada elemento en la secuencia
'''

# Ejemplo for: iterar sobre una lista de números y calcular la suma total
# Defino una lista de números
numeros = [1, 2, 3, 4, 5]

# Inicializo la variable para almacenar la suma
suma_total = 0

# Uso un bucle for para iterar sobre cada número en la lista
for numero in numeros:
    suma_total += numero  # Sumo cada número a la suma total

# Imprimo el resultado final
print(f"La suma total de los números es: {suma_total}")



'''
Investigar la estructura iterativa while y crear un ejemplo. Hacer print por consola del resultado
'''
# Estructura while
'''
while condición:
    Código que se ejecuta mientras la condición sea verdadera
'''

# Ejemplo while: contar hasta 5 e imprimir los números
# Inicializo la variable contador
contador = 1

# Uso un bucle while que se ejecuta mientras el contador sea menor o igual a 5
while contador <= 5:
    print(contador)  # Imprimo el valor actual del contador
    contador += 1    # Incremento el contador en 1

# Mensaje final después de que el bucle ha terminado
print("He terminado de contar hasta 5.")