'''
Crie uma lista que contenha todas os tipos de dados, String, int, float e boleano.
Para cada item vc deve exibir seu conteúdo, mostrar qual o seu tipo e também qual a
sua posição.
'''

lista = ["Laranja", 200, 2.5, (5 > 1)]

print(lista)
for valor in lista:
    print(f'O item {valor} é do tipo {type(valor)} e está na posição {lista.index(valor)}')