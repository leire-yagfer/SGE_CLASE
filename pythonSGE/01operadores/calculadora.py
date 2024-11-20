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

#Mostrar los resultados por pantalla
print("\nResultados:")
    #muestro diferentes formas de mostrar los valores de las variables
print(f"Suma: {num1} + {num2} = {suma}")
print("Resta: " + str(num1) + " - " + str(num2) + " = " + str(resta)) #pongo str para pasarlo a String ya que es una cadena
print("Multiplicación: {} * {} = {}".format(num1, num2, multiplicacion))
print("División: %d / %d = %.2f" % (num1, num2, division)) #ejemplo con dos decimales
print(f"Resto: {num1} % {num2} = {resto}")