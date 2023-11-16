# try:
#     # comandos
#
# except nome_exceção:
#     # comandos

# divisão por dois números
# numero1 = int(input('Entre com o primeiro número: '))
# numero2 = int(input('Entre com o segundo número: '))
# try:
#     resultado = numero1 / numero2
#     print("O resultado é: ", resultado)
#
# except ZeroDivisionError:
#     print("Não é possível divisão por zero")
# input('Pressione ENTER para sair...')
try:
    numero1 = float(input('Entre com o primeiro número: '))
    numero2 = float(input('Entre com o segundo número: '))
    resultado = numero1 / numero2
    print("O resultado é: ", resultado)

except ZeroDivisionError:
    print("Não é possível divisão por zero")
except ValueError:
    print("Valor inválido!!!")
input('Pressione ENTER para sair...')