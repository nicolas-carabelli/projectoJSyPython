##
# Pequeño web scaper que nos permite obtener los Títulos de los productos de un website
# Se cumplen las convenciones PEP8 
##
# Librería para trabajar expresiones regulares
import re
# Librería para request http
import requests

# Sitio web donde realizaremos el scraping
WEBSITE = "https://umusicstore.com.ar/collections/taylor-swift"
# Variable que realiza la petición http
resultado = requests.get(WEBSITE)
# Variable que almacena el resultado de la petición
content = resultado.text    

# Búsqueda de un patrón en una expresión que almacena los títulos de los productos
PATRON = r"/collections/taylor-swift/products/[\w-]*"
titulos_repetidos = re.findall(PATRON, str(content))
sin_duplicados = list(set(titulos_repetidos))

# Modificación para obtener solo el título de la expresión
titulos_final = []
for i in sin_duplicados:
    nombre_titulos = i.replace("/collections/taylor-swift/products/", "")
    titulos_final.append(nombre_titulos)  
    print(nombre_titulos)