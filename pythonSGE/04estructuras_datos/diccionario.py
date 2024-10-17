'''
Investigar la estructura de datos llamada diccionario. Poner ejemplos de inserción, borrado, actualización y ordenación.
'''


"""
Diccionario: se usan {} igual que en un set; pero el formato de los datos que se guarda
es clave:valor. En Python, los diccionarios son ordenados (pero no en otros lenguajes)
Clave: punto de acceso para llegar a un dato
"""
my_dict: dict = {"name":"Ana", #my_dict: dict --> declaro que my_dic es de tipo diccionario (mapa), pero no haría falta porque la estructura es de tipo diccionario
                 "surname":"Alonso", 
                 "level":"2DAM", 
                 "age":"26"
                 }
print(type(my_dict))
print(my_dict)

# Insertar elemento: acceder al dato que queremos insertar, por clave
print(my_dict["name"]) # acceso 

# Intenta acceder a la clave email; como no existe, lo inserta
my_dict["email"] = "ana@yahoo.es" # inserción
print(my_dict)

# Actualizar elementos
my_dict["age"] = 54
print(my_dict)

# Eliminar un elemento
del my_dict["email"]
print(my_dict)

# Ordenación: se usa la operación items que devuelve el conjunto de claves y valores
my_dict = dict(sorted(my_dict.items()))
print(my_dict)