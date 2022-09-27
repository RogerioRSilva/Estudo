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
#Trocando o valor em um item especificio dentro do dicionário
aluno ['nome'] = 'Jose'

print(aluno)

#Atualizando mais de um valor dentro do dicionário 
aluno.update({
    'nome': 'Marcelo',
    'nota_final': 'B'
})

print(aluno)

#Acrescentando um valor dentro do dicionário onde o memso sempre será o ultimo item. 
aluno.update({'endereço': 'Rua A'})
print(aluno)

#Utilizando o metdo GET com mensagem de erro caso não encontre o valor
print(aluno.get('Genero','Não foi encontrado!!!'))

aluno.update({
    'Genero': 'Masculino'
})
print('====== Foi inserido o item genero com o valor masculino: ============')
print(aluno)
print(aluno.get('Genero','Não foi encontrado!!!'))

#Fazendo uma remoção de um item dentro do dicionário
print('=' * 100)
print('Remoção do item GENERO do dicionário:')
del aluno['Genero']
print(aluno)

