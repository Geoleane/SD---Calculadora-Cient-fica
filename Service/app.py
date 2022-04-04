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

@app.route('/subtracao')
def subtracao():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = valor1 - valor2
        
    return jsonify(result)

@app.route('/divisao')
def divisao():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = valor1 / valor2
        
    return jsonify(result)       

@app.route('/multiplicacao')
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
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.sqrt(valor1)
        
    return jsonify(result) 

@app.route('/fatorial')
def fatorial():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.factorial(valor1)
        
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
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.sin(valor1)
        
    return jsonify(result) 

@app.route('/cosseno')
def cosseno():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.cos(valor1)
        
    return jsonify(result) 

@app.route('/tangente')
def tangente():
    v1 = request.args.get('valor1')
    v2 = request.args.get('valor2')

    valor1 = int(v1)
    valor2 = int(v2)
    result = m.tan(valor1)
        
    return jsonify(result) 

if __name__ == '__main__':
    app.run(debug=True)