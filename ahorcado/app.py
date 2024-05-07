from flask import Flask, render_template, request, redirect, url_for
import random

# Inicializamos la aplicación de Flask
app = Flask(__name__)

# Lista de palabras para el juego
palabras = ['apasionado', 'intenso', 'emocional', 'conmovedor', 'revelador', 'melancolico', 'apasionante', 'profundo']

def elegir_palabra():
    """
    Función para elegir una palabra al azar de la lista de palabras.
    """
    return random.choice(palabras)

def mostrar_letras(palabra, letras_adivinadas):
    """
    Función para mostrar las letras adivinadas y las no adivinadas de la palabra.
    """
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado


@app.route('/')
def inicio():
    """
    Función que renderiza el template de inicio del juego.
    """
    palabra = elegir_palabra()
    intentos_restantes = 6
    letras_adivinadas = []
    return render_template('inicio.html', palabra=palabra, letras_adivinadas=letras_adivinadas, intentos_restantes=intentos_restantes, mostrar_letras=mostrar_letras)


@app.route('/jugar', methods=['POST'])
def jugar():
    """
    Función que maneja la lógica del juego.
    """
    palabra = request.form['palabra']
    letra = request.form['letra']
    letras_adivinadas = request.form.getlist('letras_adivinadas[]')
    intentos_restantes = int(request.form['intentos_restantes'])

    letras_adivinadas.append(letra)
    if letra not in palabra:
        intentos_restantes -= 1

    if intentos_restantes == 0:
        return redirect(url_for('perder', palabra=palabra))
    elif mostrar_letras(palabra, letras_adivinadas).replace(' ', '') == palabra:
        return redirect(url_for('ganar', palabra=palabra))
    else:
        return render_template('jugar.html', palabra=palabra, letras_adivinadas=letras_adivinadas, intentos_restantes=intentos_restantes, mostrar_letras=mostrar_letras)


@app.route('/perder')
def perder():
    """
    Función que renderiza el template de perder el juego.
    """
    palabra = request.args.get('palabra')
    return render_template('perder.html', palabra=palabra)


@app.route('/ganar')
def ganar():
    """
    Función que renderiza el template de ganar el juego.
    """
    palabra = request.args.get('palabra')
    return render_template('ganar.html', palabra=palabra)


if __name__ == '__main__':
    app.run(debug=True)

