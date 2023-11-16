'''
A função lambda na realidade não é uma função e sim uma expressão ou também conhecida como função anônima (sem nome).
Dai, já percebemos a diferença para uma função que é denominada, nós não podemos chama-la pelo nome (já que não tem!).

lambda parâmetros: expressão
'''

import math

num = lambda: math.sqrt(81)
print(num())