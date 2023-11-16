numbers = [1, 2, 3 ,10, 20, 0.2]

# gera um vetor de numeros atravez da string
n_list = [ int(x) for x in len(numbers) ]

n_min = min(n_list)
n_pos = n_list.index(n_min) # pega a posição do valor n_min

print(f'Menor valor: {n_min}')
print (f'Posição: {n_pos}')