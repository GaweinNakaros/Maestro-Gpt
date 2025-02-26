from flask import Flask, jsonify

app = Flask(__name__)  # Inicializamos la aplicación Flask

@app.route('/saludo', methods=['GET'])  # Definimos una ruta (endpoint)
def saludo():
    return jsonify({"mensaje": "¡Hola, Matías! Bienvenido a Flask 🚀"}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Iniciamos el servidor en modo debug
