'''(
Crie um programa onde receba 3 nomes e os armazene na lista.
Mostre em seguida o nome e a posição que o nome se encontra. Para isso vc deve usar
uma funça da lista que retorne o index do item.
'''

lista = []

for c in range(0, 3):
    lista.append(input(f"Digite o {c+1}º nome: "))

print(50*"=-")
print(lista)

for c in range(0, 3):
    print(f'O nome {lista[c]} está na posição {lista.index(lista[c])}')