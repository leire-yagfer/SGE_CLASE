'''
Investigar cómo crear un fichero de tipo texto en la raíz del proyecto (o ruta elegida)
'''


"""
Manejo de ficheros
En Python, se usa import os (operaciones que interactuan con el SSOO)
"""

import os
file_name = "fichero.txt"


# Usar el manejo seguro de archivos (with)
"""En python se usa with y as para abrir (o crear si no existe), en la raíz del proyecto,
el archivo en modo escritura. Con el bloque with...as el archivo se cierra automáticamente
después de la ejecución del bloque
"""
with open(file_name, "w") as file:
    file.write("Prueba de nombre\n")
    file.write("45\n")
    file.write("Python\n")


# Imprimir el contenido del fichero 
"""
Si ponemos esta línea directamente da un error porque no tenemos permiso de lectura
sobre el fichero:
    file.read()
"""
with open(file_name, "r") as file:
    print(file.read())

# Eliminar el archivo 
    # os.remove(file_name)

