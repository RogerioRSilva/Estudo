cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']

print(cidades)
print(60 * '=')
print()
# Insere um valor na sequencia da lista, sendo esse no final da lista
cidades.append('Santa Catarina')

print(cidades)
print(60 * '=')
print()
# Remove um valor específico da lista
cidades.remove('Salvador')

print(cidades)
print(60 * '=')
print()
# Insere um valor na posição específicada do INDEX.
cidades.insert(1,'Franca')

print(cidades)
print(60 * '=')
print()

#Retira um valor da posição especificado do index
cidades.pop(0)
print(cidades)
print(60 * '=')
print()

#Organiza a lista de forma ordenada numericamente ou alfabéticamente. 
cidades.sort()
print(cidades)
print(60 * '=')
print()

print(cidades[0])

