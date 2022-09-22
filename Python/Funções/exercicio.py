def soma(x,y):
    resultado = x + y
    return resultado
x = 10
y = 20

print(soma(x,y))


print(80*'=')

def media(*num):
    resultado = 0
    for numeros in num:
        resultado += numeros
        media_soma = resultado / 2
    return media_soma

print(f'A média final é: {media(10,20,30,25,45)}')
