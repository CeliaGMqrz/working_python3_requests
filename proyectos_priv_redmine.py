#2. Programa que muestre el nombre de los proyectos de la aplicación redmine de nuestro ciclo. 
#Para ello necesitas autentificarte con la API key. Utiliza la respuesta XML.

# Importante!!
# Si queremos subir este programa a github, debería buscar algún mecanismo para no guardar nuestra key en el repositorio público de github.
# Para ello vamos a usar variables de entorno.

# Deremos exportar la clave de nuestra cuenta en una variable de entorno desde la terminal:
# export key ="**************************"

#Lo primero es importar la librería requests
import requests
#Importamos también la herramienta para leer xml 
from lxml import etree
#Importar la librería os que va leer nuestra variable de entorno
import os

#Es importante crear una variable donde se almacena la url base para no repetirla constantemente.
url_base="https://dit.gonzalonazareno.org/redmine/"

#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["key"]

#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'key':key}

#Hacemos la petición, guardandola en una variable r, añadiendo los parametros que necesitamos usando params e indicando el diccionario creado previamente.
r=requests.get(url_base+'projects.xml',params=payload)

#Para asegurarnos que no hay errores consultamos el estado de la petición.

if r.status_code == 200:
    #Convertimos r.text en un arbol xml.// fromstring carga el xml desde una variable string.//Hay que codificarlo a utf-8 para que no de un error(api redmine)
    doc = etree.fromstring(r.text.encode('utf-8'))
    #Con xpath cogemos el name
    proyectos=doc.xpath("project/name/text()")
    #Tenenmos que recorrer la lista que devuelve el xpath
    for proyecto in proyectos:
        print(proyecto)
