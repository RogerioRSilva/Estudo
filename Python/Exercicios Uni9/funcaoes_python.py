'''
Para criarmos as funções em Python, é necessário utilizar a cláusula def e a sintaxe básica é:

def nome_funcao (parâmetros):

            instruções
'''

import math

def raizQuadrada():
    return math.sqrt(81)

print(raizQuadrada())

# Função recebendo parametros
def raizQuadrada(num1, num2):
	num1 = math.sqrt(num1)
	num2 = math.sqrt(num2)
	return num1,num2

print(raizQuadrada(81, 9))