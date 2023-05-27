try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números.')
else:
    print('Valor gravado!!!')
    resultado = valor * 2
    print(resultado)   # Executa somente se o try for executado

# finally é sempre executado em todos os casos.
