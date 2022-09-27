# Google built-in functions 

# Map Function
    # Muito Utilizado com listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dic, etc..)

lista1 = [1, 2, 3, 4]

def mult (x):
    return x * 2

#Aqui estou usando a função map para 'mapear a lista' e utilizar cada 
# item dentro da função mult

lista2 = map(mult, lista1)

#Aqui fiz a conversão da variavel lista2 em lista usando a função 'list'.
print(list(lista2))

