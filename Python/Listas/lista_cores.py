cor_cli = input('Digite a cor desejada: ')
cores = ['Amarelo', 'Verde', 'Azul','Vermelho']


#O recurso lower() a frente da variável faz com que o valor a ser procurado seja colocado sempre em letras minusculas. Facilitando
# a busca dos dados dentro do array. 

if cor_cli.lower() in cores:
    print('SIM!!!')
else:
    print('NÃO.')

    