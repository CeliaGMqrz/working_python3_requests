# Introducción a la librería python requests

### Instalar la librería

``pip install requests``

> En este caso estamos usando una entorno virtual con flask

### Utilizar requests en la consola de python3

- Importamos la libreria requests y hemos guardado en una variable todo el contenido que nos ha devuelto la api de swapi según los parámetros introducidos.
`` import requests ``
``r=requests.get("https://swapi.dev/api/people/1/") `` 
``r ``
- La variable r es una respuesta 200.
```{r}
Response [200] 
```

- Es muy importante saber el estado de la respuesta porque si nos devuelve un 404 no tendremos información. Para ello usaremos 'variable.status_code'
`` r.status_code``
```{r}
200
```

- Es de utlidad saber a qué url le estamos haciendo la petición de la siguiente forma
`` r.url ``
```{r}
'https://swapi.dev/api/people/1/'
```

- Para mostrar el cuerpo o contenido de la respuesta podemos hacerlo como cadena usando 'r.text' o como diccionario usando 'r.json()'

``r.text``
```{r}
'{"name":"Luke Skywalker","height":"172","mass":"77","hair_color":"blond","skin_color":"fair","eye_color":"blue","birth_year":"19BBY","gender":"male","homeworld":"http://swapi.dev/api/planets/1/","films":["http://swapi.dev/api/films/1/","http://swapi.dev/api/films/2/","http://swapi.dev/api/films/3/","http://swapi.dev/api/films/6/"],"species":[],"vehicles":["http://swapi.dev/api/vehicles/14/","http://swapi.dev/api/vehicles/30/"],"starships":["http://swapi.dev/api/starships/12/","http://swapi.dev/api/starships/22/"],"created":"2014-12-09T13:50:51.644000Z","edited":"2014-12-20T21:17:56.891000Z","url":"http://swapi.dev/api/people/1/"}'
``` 
``r.json()``
```{r}
{'vehicles': ['http://swapi.dev/api/vehicles/14/', 'http://swapi.dev/api/vehicles/30/'], 'starships': ['http://swapi.dev/api/starships/12/', 'http://swapi.dev/api/starships/22/'], 'edited': '2014-12-20T21:17:56.891000Z', 'skin_color': 'fair', 'homeworld': 'http://swapi.dev/api/planets/1/', 'height': '172', 'created': '2014-12-09T13:50:51.644000Z', 'eye_color': 'blue', 'birth_year': '19BBY', 'hair_color': 'blond', 'films': ['http://swapi.dev/api/films/1/', 'http://swapi.dev/api/films/2/', 'http://swapi.dev/api/films/3/', 'http://swapi.dev/api/films/6/'], 'species': [], 'url': 'http://swapi.dev/api/people/1/', 'gender': 'male', 'mass': '77', 'name': 'Luke Skywalker'}
``` 