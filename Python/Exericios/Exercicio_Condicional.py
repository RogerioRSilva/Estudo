'''
Crie um script para calcular o desconto do INSS, de acordo com o salario informado pelo Usuário,
conforme tabela de desconto abaixo:

Salário                                      Desconto

Até R$ 1693,72                               8%

De R$ 1693,73 a R$ 2822,90                   9%

De R$ 2822,91 a R$ 5645,80                  11%

Acima de R$ 5645,80                O desconto é de R$ 621,04.
'''

salario = float(input("Digite o valor do seu salário: R$"))


if salario <= 1693.72:
    inss = round((salario * 0.08), 2)
    reajuste = round(inss - salario, 2)
    print(f'Seu salario com desconto do INSS de R${inss} que é 8%: R${abs(reajuste)}')

elif salario > 1693.73 and salario <= 2822.90:
    inss = round((salario * 0.09), 2)
    reajuste = round(inss - salario, 2)
    print(f'Seu salario com desconto do INSS de R${inss} que é 9%: R${abs(reajuste)}')

elif salario > 2822.90 and salario <= 5645.80:
    inss = round((salario * 0.11), 2)
    reajuste = round(inss - salario, 2)
    print(f'Seu salario com desconto do INSS de R${inss} que é 11%: R${abs(reajuste)}')

else:
    inss = 621.04
    reajuste = salario - inss
    print(f'Seu salario com desconto do INSS e de R${inss}: R${abs(reajuste)}')