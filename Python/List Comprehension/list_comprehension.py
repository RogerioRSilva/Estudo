# List Comprehension
    # Mais simples de escrever
    # Utilizado quando vc precisa criar uma nova lista a partir de uma existente
    # [expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

frutas2 = []

for iten in frutas1:
    if 'b' in iten:
        frutas2.append(iten)


frutas3 = [iten for iten in frutas1 if 'n' in iten]

print(frutas2)
print(frutas3)


#==========================================

valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)

valores2 = [x*10 for x in range(6)]

print(valores2)





