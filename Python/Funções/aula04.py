# def soma(*num):
#     return num

# x = soma(2,3,4,5)

# print(x)

def soma(*num):
    resultado = 0
    for numeros in num:
        resultado += numeros
    return resultado

x = soma(2,3,4,5)

print(x) 