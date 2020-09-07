# Put your app in here.

from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    return 'home'

@app.route('/add')
def addition():
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(add(a, b))
    
@app.route('/sub')
def subtraction():
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(sub(a, b))
    
@app.route('/mult')
def multiply():
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(mult(a, b))
    
@app.route('/div')
def divide():
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return str(div(a, b))

# Further Study

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def calc(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(operations[operation](a, b))