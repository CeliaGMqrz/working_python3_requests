#ej5 Crear un programa que utilizando la API de openwheathermap pida el nombre de una ciudad por teclado y muestre su temperatura actual.
import requests
from lxml import etree
import os 
url_base="https://api.openweathermap.org/data/2.5/"
key=os.environ["key"]
#Pedimos la ciudad
ciudad= input("Introduce una ciudad: ")
#Introducimos todos los parametros necearios en el diccionario
payload= {'q': ciudad, 'mode':'xml','units':'metric','APPID':key}
#añadimos a la variable r el contendido de la petición.
r=requests.get(url_base+'weather',params=payload)
#comprobamos que nos devuelve bien el contenido
if r.status_code == 200:
    doc = etree.fromstring(r.text.encode('utf-8'))
    #buscamos por medio de el arbol la temperatura de la ciudad indicando el valor primero.
    temp=doc.xpath("temperature/@value")[0]
    print(temp+" ºC")