produtos = ['arroz', 'feijão', 'laranja', 'banana']

item1 = produtos[0]

print(produtos)
print('Extraiu da lista:', item1)
print()

item1, item2, item3, item4 = produtos

print('Extraiu da lista item1:', item1)
print('Extraiu da lista item2:', item2)
print('Extraiu da lista item3:', item3)
print('Extraiu da lista item4:', item4)


# dessa forma podemos buscar os itens mencionados e isolar os
# outros
item1, item2, item3, *outros = produtos

print(item1, item2, item3)
