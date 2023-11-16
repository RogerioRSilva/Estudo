'''
A linguagem Python já traz implantada em sua biblioteca a classe turtle (tartaruga) com muitas funções.
Vamos ver algumas delas, mas incentivo a explorar mais os recursos dessa classe.
'''


from turtle import *
# movimentando a tartaruga
shape("turtle") # coloca o formato da tartaruga
delay(50)
forward(200) # anda para frente 100 pixels
right(90)   # vira 90 graus para direita
forward(200)
right(90)
forward(200)
right(90)
forward(200)


from turtle import *
# movimentando a tartaruga
title("TARTARUGA TOUCHE!") # coloca o título na janela
bgcolor("lightyellow") # coloca a cor de fundo da janela em amarelo claro
pensize(4)  # define a espessura do traço
color("blue") # cor da tartaruga e do traço
shape("turtle") # coloca o formato da tartaruga
delay(50)
for cont in range(4):
    forward(200) # anda para frente 100 pixels
    right(90)   # vira 90 graus para direita

from turtle import *


# movimentando a tartaruga

def quadrado(graus, tamanho):
    for cont in range(4):
        forward(tamanho)
        right(graus)


def triangulo(graus, tamanho):
    for i in ["red", "violet", "orange"]:
        color(i)
        left(graus)
        forward(tamanho)


def touche():
    title("TARTARUGA TOUCHE!")  # coloca o título na janela
    bgcolor("lightyellow")  # coloca a cor de fundo da janela em amarelo claro
    pensize(4)  # define a espessura do traço
    color("blue")  # cor da tartaruga e do traço
    shape("turtle")  # coloca o formato da tartaruga
    delay(50)
    quadrado(90, 200)
    triangulo(120, 150)


touche()  # Chama a função
exitonclick()  # aguarda o clique do mouse para encerrar