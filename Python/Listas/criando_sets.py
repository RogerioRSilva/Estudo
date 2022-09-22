list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

print(list1)
print(list2)
print()

num1 = set(list1)

num2 = set(list2) 

print(num1)

print(num2)
print()

print(num1 | num2) #Union = uni duas listas excluindo repetições.
print()
print(num1 - num2) #Difference = Faz comparativo entre as duas listas e mosta somente o que é diferente. 
print()

print(num1 ^ num2) #Symetric Difference = Faz a união das duas tabelas removendo das duas tabelas os repetidos. 
print()

print(num1 & num2) #and - Mostra somente o que está repetido nas duas listas
print()

print(len(num1)) #len - Faz a contagem da quantidade de itens na lista. 


