'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

listaFuncionarios = ["Marcelo", "João", "Heloisa", "Michele", "Juliana", "Isadora", "Vinicius", "Arthur"]
listaFuncionarios_noite = ["Marcelo", "Juliana", "Isadora", "João"]
listaFuncionarios_dia = ["Heloisa", "Michele", "Vinicius", "Arthur"]
listaTemCarro = ["Marcelo", "Michele", "Juliana", "Vinicius"]

lista1 = set(listaFuncionarios_noite).intersection(listaTemCarro)
print("Funcionarios que trabalham a noite e tem carro: ", lista1)

lista2 = set(listaFuncionarios_dia).intersection(listaTemCarro)
print("Funcionarios que trabalham de dia e tem carro: ", lista2)

lista3 = set(listaFuncionarios).difference(listaTemCarro)
print("Funcionarios que não tem carro: ", lista3)
