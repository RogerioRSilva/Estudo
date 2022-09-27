# Dicionários
    # Utiliza index no formato de Keys e values
    # Aceita string, integer, float, boolean...

#Dicionário Criado com itens e variaveis diversas. 
aluno = {
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'Aprovação': True
    
    }
#Aqui conseguimos imprimir somente as Keys ou itens ou chaves do dicionário.
print('Somente as KEYS:')
for x in aluno.keys():
    print(x)

print('=' * 100)

# Aqui faz a impressão somente dos valores de cada keys/chaves/itens  
print('Somente os valores das Keys:')  
for x in aluno.values():
    print(x)

print('=' * 100)
#Aqui o comando faz a impressão de cada item completo do dicionário
print('Os valores de todos os itens do dicionário:')
for x in aluno.items():
    print(x)

#Aqui o comando faz a impressão de cada item separadamente porem fora de uma tupla.
for a, b in aluno.items():
    print(f' A Key {a}: com o Value {b}')

