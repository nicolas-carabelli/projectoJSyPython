from flask import Flask, request, jsonify, render_template
import curses

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['POST'])
def draw():
    # Recibir datos de dibujo desde el script de JavaScript
    data = request.get_json()
    # Dibujar en la ventana de curses utilizando Python
    # ...
    return jsonify({'message': 'Dibujo realizado con éxito'})

if __name__ == '__main__':
    app.run(debug=True)
