from flask import Flask, jsonify
from flask import Blueprint
from datetime import date
import json
import os

from utils.aes import encrypt
from utils.hash import hashGenerator


import requests

# app = create_app()
app = Flask(__name__)


    

# Agregar autenticacion para que solo los usuarios autorizados puedan acceder a los datos

# Agregar machinlearning para saber como identificar los medicamentos falsificados por region y por pais en costos y precios.

# Agregar un hash para que los datos sean incorruptibles y no se puedan modificar

# Unidades unicas para verificar que los valores de los medicamentos sean correctos y no duplicados y sea su llave primaria para medicamentos.

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Estatus del servicio
@app.route('/status')
def status():
    return jsonify(
        commit__version="1.0.1",
        release__version="1.0.0",
        status="ok",
        date=date.today(),
    )

# Consumo de la informacion
@app.route('/mook')
def mook():
    path = "/model"
    filename = os.path.join("model", 'mook.json')
    with open(filename) as data_file:
        mook_data = json.load(data_file) 
        return mook_data

# Agregar encriptacion para verificar que los datos sean incorruptibles. Aes256 o RSA 4096
# Consumimos servicios de AES y Hash Tables

@app.route('/service/aes/encrypt/<data>')
def aes(data):
    hashValue = hashGenerator(data)
    encriptacion = encrypt(data)
    return f'The about page {encriptacion}'


if __name__ == '__main__':
    app.run(debug=True)