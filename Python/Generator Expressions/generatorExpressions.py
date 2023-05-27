#Generator Expressions
    # Uma forma mais rápida para listas, dicionários e etc
    # Menos memória alocada
    # VAlores em bytes

from sys import getsizeof

numeros = [x * 10 for x in range(1000)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print()
print("=============================")
print()

numeros = (x * 10 for x in range(1000)) #Utilizando o Generator Expression (Transforma em objeto)
print(type(numeros))
print(numeros)
print(getsizeof(numeros)) # Quantidade de memória utilizada
