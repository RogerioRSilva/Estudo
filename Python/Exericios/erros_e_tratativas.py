# Erros
    # Excelente para testes
    # Não realiza o 'STOP' no programa
    # Mensagens customizadas quando encontra um erro

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe...')

print()
####################################################
try:
    valor = int(input('Digite o valor: R$ '))
    print('R$', valor)
except ValueError:
    print('Valor incorreto - Digite o valor em números inteiros...')

print('Mais codigos abaixo.')

print()
print(60*'#')
###################################################

try:
    valor = int(input('Digite o valor: R$ '))
    print('R$', valor)
except ValueError:
    print('Valor incorreto - Digite o valor em números inteiros...')
# else:
#     print('Valor inserido = ', valor)
finally:
    print('Valor inserido = ', valor)

