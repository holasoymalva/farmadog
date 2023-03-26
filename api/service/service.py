from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about/<name>')
def about(name):
    return f'The about page {name}'

if __name__ == '__main__':
    app.run(debug=True)