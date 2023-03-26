from flask import Flask
import requests

app = Flask(__name__)

mook_data = {
    'medicamento_1': {
        'id': 1,
        'nombre': 'aspirina',
        'descripcion': 'Medicamento para el dolor de cabeza',
        'lote': 'X24AU3'
    },
    'medicamento_2': {
        'id': 2,
        'nombre': 'Omeprazol',
        'descripcion': 'Medicamento para el dolor de estomago',
        'lote': 'M216-05'
    },  
    'medicamento_3': {
        'id': 3,
        'nombre': 'Sentralina',
        'descripcion': 'Medicamento para el dolor de cabeza',
        'lote': 'U22S335'
    },
    'medicamento_4': {
        'id': 4,
        'nombre': 'Paracetamol',
        'descripcion': 'Medicamento para el dolor de cabeza',
        'lote': 'U22S335'
    },
}

# Agregar encriptacion para verificar que los datos sean incorruptibles. Aes256 o RSA 4096

# Agregar autenticacion para que solo los usuarios autorizados puedan acceder a los datos

# Agregar machinlearning para saber como identificar los medicamentos falsificados por region y por pais en costos y precios.

# Agregar un hash para que los datos sean incorruptibles y no se puedan modificar

# Unidades unicas para verificar que los valores de los medicamentos sean correctos y no duplicados y sea su llave primaria para medicamentos.

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about/<name>')
def about(name):
    return f'The about page {name}'

@app.route('/mook')
def mook():
    return mook_data

if __name__ == '__main__':
    app.run(debug=True)