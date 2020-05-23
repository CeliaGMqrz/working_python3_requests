#4. Programa que pida el nombre de un proyecto del redmine de nuestro ciclo y que muestre las 5 últimas tareas abiertas del proyecto indicado.
# Si no existe el proyecto da un error.

# Importante!!
# Si queremos subir este programa a github, debería buscar algún mecanismo para no guardar nuestra key en el repositorio público de github.
# Para ello vamos a usar variables de entorno.

# Deremos exportar la clave de nuestra cuenta en una variable de entorno desde la terminal:
# export key ="**************************"

#Lo primero es importar la librería requests
import requests
#Importamos etree 
from lxml import etree
#Importar la librería os que va leer nuestra variable de entorno
import os

#Es importante crear una variable donde se almacena la url base para no repetirla constantemente.
url_base="https://dit.gonzalonazareno.org/redmine/"

#En una variable key, guardamos por el diccionario os.environ nuestra key
key=os.environ["key"]

#Vamos a crear un diccionario que guarde nuestros parámetros
payload = {'key':key}
#Pedimos el nombre del proyecto
nom_proyecto=input("\nIntroduce el nombre del proyecto: ")
#Necesitaremos el identificador del proyecto
id_project=""
#Hacemos la petición, guardandola en una variable r, añadiendo los parametros que necesitamos usando params e indicando el diccionario creado previamente.
r=requests.get(url_base+'projects.xml',params=payload)



#Para asegurarnos que no hay errores consultamos el estado de la petición.
pjs=[]
if r.status_code == 200:
    #Guardamos en la variable doc el contenido leido en json
    doc = etree.fromstring(r.text.encode('utf-8'))
    #Obtenemos los nombres de los proyectos
    projects=doc.xpath("project")
    for p in projects:
        if p.xpath("name/text()")[0] == nom_proyecto:
            id_project=p.xpath("id/text()")[0]


payload = {'status_id':'open','limit':'5','project_id':id_project,'key':key}
r=requests.get(url_base+'issues.xml',params=payload)
if r.status_code == 200:
	doc = etree.fromstring(r.text.encode ('utf-8'))
	tareas=doc.xpath("issue")
	for t in tareas:
		print (t.xpath("assigned_to/@name")[0])
		print (t.xpath("subject/text()")[0])
else:
	print ("Error de proyecto")