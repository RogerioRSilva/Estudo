import math

print("########## CALCULADORA DE IMC ############\n")

altura = float(input('Qual a sua altura: ').replace(',', '.'))
peso = float(input('Qual o seu peso: ').replace(',', '.'))

imc = round(peso / (math.pow(altura, 2)), 2)

if (imc < 18.5):
    print(f'Seu IMC é: {imc} e vc está muito magro.')

elif (imc >= 18.5 and imc < 24.9):
    print(f'Seu IMC é: {imc} e vc está Ideal.')

elif (imc >= 24.9 and imc < 29.9):
    print(f'Seu IMC é: {imc} e vc está com sobrepeso.')

elif (imc >= 29.9 and imc < 39.9):
    print(f'Seu IMC é: {imc} e vc está obeso.')

else:
    print(f'Seu IMC é: {imc} e vc está com obesidade morbida.')