"""
from flask import Flask, jsonify

app = Flask(__name__)  # Inicializamos la aplicación Flask

@app.route('/saludo', methods=['GET'])  # Definimos una ruta (endpoint)
def saludo():
    return jsonify({"mensaje": "¡Hola, Matías! Bienvenido a Flask 🚀"}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Iniciamos el servidor en modo debug
"""


"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saludo/<nombre>', methods=['GET'])  # Ruta dinámica

def saludo_personalizado(nombre):
    return jsonify({"mensaje": f"¡Hola, {nombre}! Bienvenido a Flask 🚀"}), 200 #Convierte automáticamente listas y diccionarios de Python a JSON.

if __name__ == '__main__':
    app.run(debug=True)
"
"""
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.json  # Recibe el JSON enviado por el cliente
    num1 = data.get('num1', 0)  # Obtiene el primer número, si no existe usa 0
    num2 = data.get('num2', 0)  # Obtiene el segundo número, si no existe usa 0
    resultado = num1 + num2

    return jsonify({"resultado": resultado})  # Devuelve la suma en JSON

if __name__ == '__main__':
    app.run(debug=True)
"""
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "¡Hola, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
"""

#FastAPI API con POST
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # FastAPI usa Pydantic para validar que los datos sean números enteros.

class SumaRequest(BaseModel):
    num1: int
    num2: int

@app.post("/suma")
def sumar(datos: SumaRequest):
    return {"resultado": datos.num1 + datos.num2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


#FastAPI genera automáticamente documentación en Swagger y Redoc.

#🔍 Para ver Swagger UI, accede a: 📌 http://127.0.0.1:8000/docs

#🔍 Para ver Redoc, accede a: 📌 http://127.0.0.1:8000/redoc    
