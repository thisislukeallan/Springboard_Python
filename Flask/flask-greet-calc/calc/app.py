from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def m_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a, b))

@app.route('/sub')
def m_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a, b))

@app.route('/mult')
def m_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a, b))

@app.route('/div')
def m_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a, b))

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<eq>')
def math(eq):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(operations[eq](a, b))