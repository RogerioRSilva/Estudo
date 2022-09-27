#Dicionário Criado com itens e variaveis diversas. 
aluno = {
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'Aprovação': True,
    #lista dentro do dicionário
    'Materias': ['Fisica', 'Matematica', 'Ingles']
}


print(aluno)

print(aluno.get('Materias'))
print(f'Tenho {len(aluno)} itens dentro do dicionario.')
print()
print('=' * 100)
print(aluno.items())
print(aluno.keys())
print(aluno.values())
