# Filter Function
    # Muito utilizado com listas
    # Aplicar uma função a um iterable, filtrando os items.(list, tuple, dic etc.)

valores = [10, 12, 34, 44, 57]


def remover20(x):
    return x > 20


# Função sem utilizar o filter
print(list(map(remover20, valores)))

# Com a utilização do filter ele consegue trazer os valores que estão
# na lista valores.
print(list(filter(remover20, valores)))

# Utilizando o lambda sem função definida e com o filter.
print(list(filter(lambda x: x > 35, valores)))

