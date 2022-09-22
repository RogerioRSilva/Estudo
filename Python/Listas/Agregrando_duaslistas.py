cores = ['Amarelo', 'Verde', 'Azul','Vermelho']
valores = [50, 80, 110, 150]

#O recurso ZIP agrega as duas listas na mesma sequencia de INDEX sempre começando pelo 0

duas_listas = zip(cores, valores)

print(list(duas_listas))


