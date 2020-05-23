#6. Programa que utilizando la API swapi muestre la lista de personajes, cada vez que muestre la información de
# una página preguntará si quiere seguir mostrando más personajes.
# A continuación pedirá el nombre de un personaje y te dará información sobre él.


#Lo primero es importar la librería requests
import requests
#Importamos también la herramienta para leer json 
import json


#Guardamos la url base en una variable
url_base="https://swapi.dev/api/people/"

    
