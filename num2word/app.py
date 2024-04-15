from flask import Flask, render_template, request
from num2words import num2words

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    """
    Renderiza la plantilla 'index.html' en la página de inicio.
    """
    return render_template('index.html')

# Ruta para la conversión de números
@app.route('/', methods=['POST'])
def convertir_numero():
    """
    Convierte un número ingresado a palabras y lo muestra en la página.
    """
    # Obtener el número ingresado desde el formulario
    numero = request.form['numero']
    try:
        numero = int(numero)
        # Verificar si el número es negativo
        if numero < 0:
            resultado = "No se pueden convertir números negativos a palabras"
        else:
            # Convertir el número a palabras en español
            resultado = num2words(numero, lang='es')
    except ValueError:
        # Manejar el caso de entrada no válida
        resultado = "Por favor, introduce un número válido"
    
    # Renderizar la plantilla 'index.html' con el resultado
    return render_template('index.html', resultado=resultado)

# Ejecutar la aplicación Flask si este script es el programa principal
if __name__ == '__main__':
    app.run(debug=True)
