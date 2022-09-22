numeros = [2, 3, 4, 5]
print(numeros)


final = numeros * 2
print('Duplicando a lista: ', final)

letras = ['a', 'b', 'c', 'd']

final = numeros + letras
print('Concatenando as listas: ', final)

numeros.extend(letras)
print(numeros)
print(60 *'=')
print()

#Lista dentro de lista
itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens)

