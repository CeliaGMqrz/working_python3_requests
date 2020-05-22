#3.Realiza el ejercicio 2, pero utilizando la respuesta JSON.

# Importante!!
# Si queremos subir este programa a github, debería buscar algún mecanismo para no guardar nuestra key en el repositorio público de github.
# Para ello vamos a usar variables de entorno.

# Deremos exportar la clave de nuestra cuenta en una variable de entorno desde la terminal:
# export key ="**************************"

#Lo primero es importar la librería requests
import requests
#Importamos también la herramienta para leer json 
import json
#Importar la librería os que va leer nuestra variable de entorno
import os

#Es importante crear una variable donde se almacena la url base para no repetirla constantemente.
url_base="https://dit.gonzalonazareno.org/redmine/"

#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["key"]

#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'key':key}

#Hacemos la petición, guardandola en una variable r, añadiendo los parametros que necesitamos usando params e indicando el diccionario creado previamente.
r=requests.get(url_base+'projects.json',params=payload)

#Para asegurarnos que no hay errores consultamos el estado de la petición.

if r.status_code == 200:
    #Guardamos en la variable doc el contenido leido en json
    doc = r.json()
    #Obtenemos los nombres de los proyectos
    for proyecto in doc["projects"]:
        print(proyecto["name"])
    
