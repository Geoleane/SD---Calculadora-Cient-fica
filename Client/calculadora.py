import requests

operacao = input()
valor1 = input()
valor2 = input()

link = f'http://localhost:5000/{operacao}?valor1={valor1}&valor2={valor2}'
requisicao = requests.get(link)

print (requisicao.json()) 