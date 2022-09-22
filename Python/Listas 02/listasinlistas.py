# pessoas = [['pedro',25],['maria', 19], ['joão, 32']]


# print(pessoas)
# print(pessoas[0][1])
# print(pessoas[1][0])
# print(pessoas[1])

# teste = list()

# teste.append('Gustavo')
# teste.append(40)

# galera = list()
# galera.append(teste[:])

# teste[0] = 'maria'
# teste[1] = 22

# galera.append(teste[:])#Copia da lista (teste) completa

# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# for p in galera:
#     print(p)

# print(galera[0])

# print(galera[2][1])

galera = list()
dado = list()
totalmai = totalmen = 0

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmen += 1

print(f'Temos {totalmai} maior(es) e {totalmen} menor(es) de idade.')



