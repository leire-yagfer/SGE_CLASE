'''Realizar un pequeño programa llamado calculadora.py que pida por teclado 2 números y muestre 
por pantalla estas operaciones aritméticas: suma, resta, multiplicación, división, resto.'''

# Solicitar dos números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
resto = num1 % num2

# Mostrar los resultados por pantalla
print(f"\nResultados:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
print(f"Resto: {num1} % {num2} = {resto}")
