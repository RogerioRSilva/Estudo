#Usa-se Array sempre que uma lista é muito grande. 
from array import array


letras = ['a', 'b', 'c', 'd' ]
numeros_i = [10, 20, 30, 40]
numeros_f = [1.1, 2.2, 3.3, 4.4]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd' ])
print(letras)
numeros_i = array('i', [10, 20, 30, 40])
print(numeros_i)
numeros_f = array('f', [1.1, 2.2, 3.3, 4.4])
print(numeros_f)