"""
Herencia: jerarquía entre clases. La subclase puede heredar de la clase padre 
(propiedades y métodos)
Ventaja: reutilización de código
"""

# HERENCIA
# Superclase
class Animal:
    # inicializador que recibe el parámetro name
    def __init__(self, name: str):
        self.name = name
    #defino el método sobre el sonido que hará cada animal de la subclase que cree
    def sound(self): #las clases que heredan de Animal pueden sobrescribir este método para hacer un sonido específico
        pass #indica que no se implementa ninguna funcionalidad en este método por el momento, cuando lo hereden otras clases decidirán que código contendrá


"""Subclases: heredan de la clase Animal al poner (Animal). El inicializador no lo ponemos en 
las clases Dog y Cat porque es un nombre común que lo heredan de Animal. 
En el caso de la función sound, sí se redefinen en las clases Dog y Cat.
En resumen: en este ejemplo, el inicializador es común pero la función sound se redefine
"""
        
# Clases que heredan de Animal(tienen las propiedades y métodos de Animal)    
# pueden tener sus propios métodos o sobrescribir los existentes   
class Dog(Animal): #Animal entre () pq es la superclase que hereda Dog
    def sound(self): # sobrescribe el método sound de Animal
        print("Guau")

class Cat(Animal):
    def sound(self): # sobrescribe el método sound de Animal
        print("Miau")

#creo instancias de cada clase
my_animal = Animal("Animal")
my_animal.sound() # no hace nada pq se ejecuta el método sound de la clase Animal
my_dog = Dog("Perro")
my_dog.sound()
my_cat = Cat("Gato")
my_cat.sound()


# POLIMORFISMO: capacidad de un objeto de tomar varias formas. 
""" 
En el caso anterior ya hay polimorfismo: si es un gato suena de una manera y si es
un perro, suena de otra. Es polimorfismo en tiempo de compilación.
En este caso, vamos a definir la función print_sound()
Esto es polimorfismo en tiempo de ejecución 
"""

class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        pass      
        
class Dog(Animal):
    def sound(self):
        print("Guau")

class Cat(Animal):
    def sound(self):
        print("Miau")

# función que recibe un parámetro animal (instancia de la clase Animal o de una subclase)
def print_sound(animal: Animal): 
    #llama al método sound del objeto animal que se pasa como parámetro // animal puede ser una instancia de Dog, Cat o Animal; con lo cual se ejecutará el método correspondiente
    animal.sound() #en este caso se llama al sound de la clase Animal, por lo que no hace nada

#creo instancias de Animal, Dog y Cat, y las paso a la función print_sound
my_animal = Animal("Animal")
print_sound(my_animal) # No imprime nada, ya que `Animal.sound()` no hace nada

my_dog = Dog("Perro") #creo un objeto de la clase Dog y le paso una cadena de texto, "Perro", como argumento para el inicializador (__init__)
print_sound(my_dog) # Imprime: Guau

my_cat = Cat("Gato")
print_sound(my_cat) # Imprime: Miau

""""
RESUMEN:
Herencia: Dog y Cat heredan de Animal; ambas clases tienen acceso a los métodos y atributos de Animal
Sobrescritura de métodos: las clases Dog y Cat sobrescriben el método sound() para tener su propio comportamiento
Polimorfismo: a la función print_sound() se le pueden pasar diferentes tipos de animales y la función
invocará al método sound() correspondiente según la clase del objeto que se le pase (Dog, Cat...)
"""