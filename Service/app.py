from distutils.log import debug
import json
from unittest import result
from flask import Flask, jsonify, render_template, request
import math as m

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/soma')
def soma():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = valor1 + valor2
        
    return jsonify(result)

@app.route('/subtrai')
def subtracao():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = valor1 - valor2
        
    return jsonify(result)

@app.route('/divide')
def divisao():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = valor1 / valor2
        
    return jsonify(result)       

@app.route('/multiplica')
def multiplicacao():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = valor1 * valor2
        
    return jsonify(result) 

@app.route('/eleva')
def expoente():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.pow(valor1,valor2)
      
    return jsonify(result) 

@app.route('/raiz')
def raiz():
    v = request.args.get('valor')

    valor = int(v)
    result = m.sqrt(valor)
        
    return jsonify(result) 

@app.route('/fatorial')
def fatorial():
    v = request.args.get('valor')

    valor = int(v)
    result = m.factorial(valor)
        
    return jsonify(result) 

@app.route('/log')
def log():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.log(valor1,valor2)
        
    return jsonify(result) 

@app.route('/seno')
def seno():
    v = request.args.get('valor')

    valor = int(v)
    result = m.sin(valor)
        
    return jsonify(result) 

@app.route('/cosseno')
def cosseno():
    v = request.args.get('valor')

    valor = int(v)
    result = m.cos(valor)
        
    return jsonify(result) 

@app.route('/tangente')
def tangente():
    v = request.args.get('valor')

    valor = int(v)
    result = m.tan(valor)
        
    return jsonify(result) 

if __name__ == '__main__':
    app.run(debug=True)