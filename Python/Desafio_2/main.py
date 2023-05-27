'''
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá forncer as seguintes informações: 
Rendimento, altura e largura
O programa deve mostrar na tela a mensagem 'Você necessida de X latas de tinta'
'''

from funcoes import coberturaTinta

rendimento = float(input('Qual o rendimento da tinta? '))
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

coberturaTinta(rendimento, altura, largura)
