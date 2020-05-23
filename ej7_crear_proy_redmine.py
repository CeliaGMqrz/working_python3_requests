# 7.Programa que cree un proyecto, llamado “test project” en el redmine de nuestro ciclo.

# Se trata de crear recursos, por lo que usaremos el método POST
# Se necesitarian privilegios de administrador por lo que nosotros como usuarios no podemos hacer la petición. Nos daría error.

#Lo primero es importar la librería requests
import requests
#Importar la librería os que va leer nuestra variable de entorno
import os
#Es importante crear una variable donde se almacena la url base para no repetirla constantemente.
url_base="https://dit.gonzalonazareno.org/redmine/"
#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["key"]
#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'key':key}
#Creamos el contenido que vamos a enviar por medio del método POST. Es el cuerpo de la petición POST. Con las características que queremos.

xml_project="""
<project>
    <name>test project</name>
    <identifier>test1</identifier>
    <enabled_module_names>time_tracking</enabled_module_names>
    <enabled_module_names>issue_tracking</enabled_module_names>
</project>
"""
#Crear diccionario con la cabecera de la petición. Donde pongo el tipo de contenido. Aquí le decimos a redmine que tipo de contenido
# vamos a mandar.
headers = {'Content-Type': 'application/xml'}
#Petición POST, indicamos la url, los parámentros, los datos del cuerpo 'data', y por último el parámetro headers (cabecera)
r = requests.post(url_base+'projects.xml', params=payload, data=xml_project, headers=headers)

if r.status_code == 201:
    print("ok")
else:
    print("Error: "+r.text)

