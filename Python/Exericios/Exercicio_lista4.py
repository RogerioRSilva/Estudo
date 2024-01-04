'''
Crie um programa que receba 5 valores em reais e ao chamar esse valor
o mesmo deve receber um acréscimo de 5% se ele for maior ou igual a R$ 100.00 ,
se ele for menor que R$ 100,00 o mesmo deve receber um acréscimo de 10%. Todos
os valores tem que se manter em formato de reais exibindo apenas 2 casas decimais
após a virgula. A cada inserção deve ser exibido o valor atual, o valor do
acrescimo e o valor final.
'''

lista = []
diferenca = 0
valor_atual = 0

for c in range(0, 5):
    lista.append(float(input(f'Digite o {c+1}º valor em R$.: ')))
    valor_atual = lista[c]

    if lista[c] >= 100.00:
        lista[c] = round((lista[c] * (1+0.05)), 2)
        diferenca = round(lista[c] - valor_atual, 2)
        print(f'Valor atual: R$ {valor_atual}... Acrescimo: R${diferenca}... Valor Final: R$ {lista[c]}')

    elif lista[c] < 100.00:
        lista[c] = round((lista[c] * (1 + 0.10)), 2)
        diferenca = round(lista[c] - valor_atual, 2)
        print(f'Valor atual: R$ {valor_atual}... Acrescimo: R${diferenca}... Valor Final: R$ {lista[c]}')
