from flask import Flask, render_template, request
from num2words import num2words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convertir_numero():
    numero = request.form['numero']
    try:
        numero = int(numero)
        if numero < 0:
            resultado = "No se pueden convertir números negativos a palabras"
        else:
            resultado = num2words(numero, lang='es')
    except ValueError:
        resultado = "Por favor, introduce un número válido"
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
