'''
Por exemplo, para aceitar valores iniciais de um número de celular (por exemplo, 99876-1234)
que tem 5 números de 0 a 9, podemos definir: \d{5},
onde \d representa qualquer digito entre 0 a 9 e {5} é a quantidade de números iniciais do celular (99876).

Agora se quisermos aceitar
td o número de qualquer celular, com o padrão, por exemplo: 99876 - 1234,
poderemos definir como: \d{5} - \d{4}, onde \d representa qualquer dígito de o a 9,
{5} quantidade de números iniciais, - o hífen, \d qualquer dígito de 0 a 9 e {4}  quantidade de 4 dígitos finais.
'''

# valida o número do cpf com pontos e hífens
# import re
# cpf = str(input('Entre com o número do CPF, com pontos e hífen: \n'))
# if re.search('\d{3}.\d{3}.\d{3}-\d{2}', cpf):
#     print('Número CPF validado')
# else:
#     print('Número do CPF fora do padrão')
# input('Pressione ENTER para sair...')


# valida o número do cpf som pontos e com hífen
import re
cpf = str(input('Entre com o número do CPF, com pontos e hífen: \n'))
if re.search('\d{3}\d{3}\d{3}-\d{2}', cpf):
    print('Número CPF validado')
else:
    print('Número do CPF fora do padrão')
input('Pressione ENTER para sair...')