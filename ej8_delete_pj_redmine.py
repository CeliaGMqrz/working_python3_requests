# 8. Programa que borre el proyecto creado en el ejercicio anterior.

# Se necesitarian privilegios de administrador por lo que nosotros como usuarios no podemos hacer la petición. Nos daría error.

#Lo primero es importar la librería requests
import requests
#Importar la librería os que va leer nuestra variable de entorno
import os
# Importar etree
from lxml import etree

#Crear url base
url_base="https://dit.gonzalonazareno.org/redmine/"
#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["key"]
#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'key':key}

#Hacemos una petición get para obtener los proyectos. 
r = requests.get(url_base+'projects.xml',params=payload)

#Buscar el identificador del proyecto que tenemos que borrar.
if r.status_code == 200:
    #Creamos el documento xml
    doc = etree.fromstring(r.text.encode('utf-8'))
    projects=doc.xpath("project")
    for p in projects:
        if p.xpath("name/text()")[0]=="test project":
            id_project=p.xpath("id/text()")[0]


# Hacemos la petición de tipo DELETE a la url base con el identificador que hemos buscado, con los parámetros.

r = requests.delete(url_base+'projects/%s.xml'%id_project, params=payload)

if r.status_code == 200:
    print("ok")
else:
    print("Error"+r.text)