#1. Programa que muestre el nombre de los proyectos públicos de la aplicación redmine de nuestro ciclo. Utiliza la respuesta XML

#Lo primero es importar la librería requests
import requests
#Importamos también la herramienta para leer xml 
from lxml import etree

#Es importante crear una variable donde se almacena la url base para no repetirla constantemente.
url_base="https://dit.gonzalonazareno.org/redmine/"

#Hacemos la petición, guardandola en una variable r, añadiendo el parámetro que necesitamos.
r=requests.get(url_base+'projects.xml')

#Para asegurarnos que no hay errores consultamos el estado de la petición.

if r.status_code == 200:
    #Convertimos r.text en un arbol xml.// fromstring carga el xml desde una variable string.//Hay que codificarlo a utf-8 para que no de un error(api redmine)
    doc = etree.fromstring(r.text.encode('utf-8'))
    #Con xpath cogemos el name
    proyectos=doc.xpath("project/name/text()")
    #Tenenmos que recorrer la lista que devuelve el xpath
    for proyecto in proyectos:
        print(proyecto)

