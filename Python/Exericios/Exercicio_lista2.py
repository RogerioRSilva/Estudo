'''
Crie um programa que receba 5 numeros quais quer, em uma lista e em seguida some
todos esses numeros.
'''

lista = []
soma = 0

for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}º numero: ')))
    soma = soma + lista[c]

print(lista)
print(f'A soma de todos os numeros da lista é {soma}')