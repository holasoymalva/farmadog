from flask import Flask

app = Flask(__name__)

mook_data = {
    'medicamento_1': {
        'id': 1,
        'nombre': 'Paracetamol',
        'precio': 10,
        'cantidad': 100,
        'descripcion': 'Medicamento para el dolor de cabeza',
        'lote': '112345'
    },
    'medicamento_2': {
        'id': 2,
        'nombre': 'Ibuprofeno',
        'precio': 15,
        'cantidad': 100,
        'descripcion': 'Medicamento para el dolor de cabeza',
        'lote': '112345'
    },  
    'medicamento_3': {
        'id': 3,
        'nombre': 'Aspirina',
        'precio': 20,
        'cantidad': 100,
        'descripcion': 'Medicamento para el dolor de cabeza',
        'lote': '112345'
    },
}

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