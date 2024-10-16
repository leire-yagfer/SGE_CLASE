'''
•	Incluir comentarios explicando los siguientes conceptos:
o	Servicio web
o	RESTful API
o	Protocolo HTTP
o	Peticiones HTTP
o	Respuestas HTTP: 200, 404, 500
'''
#Librería de Python para trabajar con APIs y servicios web. Se usa para 
#realizar peticiones HTTP
#Es necesario instalarla: pip install request


'''
•	Investigar cual es la librería de Python para realizar peticiones HTTP
'''
# se utiliza el requests.get('dirección http') para realizar las peticiones

'''
•	Realizar una petición para obtener una página web
'''
import requests #he tenido que hacer el pip install requests
response = requests.get("http://iesriberadecastilla.centros.educa.jcyl.es/sitio/")

'''
•	Verificar que la petición fue exitosa y mostrar por consola el contenido de la web (respuesta de la petición)
•	Si la petición no tuvo éxito, imprimir el código de error por pantalla
'''
# Una petición HTTP devuelve una respuesta (código HTTP). Si todo ha ido bien, devuelve 200
if response.status_code == 200:
    print(response.text) # devuelve el código fuente de la web; se podría ver representada en un navegador (renderizar)
else:
    print(f"Error con código {response.status_code} al realizar la petición")

