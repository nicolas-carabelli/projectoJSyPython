from flask import Flask, render_template, request
import requests

# Inicializar la aplicación Flask
app = Flask(__name__)

# Función para obtener detalles de una película por su título
def get_movie_by_title(title):
    """
    Obtiene detalles de una película usando la API de OMDB y el título proporcionado.

    :param title: Título de la película
    :return: Datos de la película en formato JSON
    """
    api_key = '825d40ea'
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={title}&y=&plot=short&r=json'
    response = requests.get(url)
    data = response.json()
    return data

# Ruta para la página de inicio
@app.route('/')
def index():
    """
    Renderiza la plantilla de inicio.

    :return: Renderizado de la plantilla 'index.html'
    """
    return render_template('index.html')

# Ruta para buscar una película
@app.route('/search', methods=['POST'])
def search():
    """
    Busca una película por su título y renderiza la plantilla con los datos de la película.

    :return: Renderizado de la plantilla 'index.html' con los datos de la película
    """
    title = request.form['title']
    movie = get_movie_by_title(title)
    return render_template('index.html', movie=movie)

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
