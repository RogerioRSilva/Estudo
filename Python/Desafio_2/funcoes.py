def coberturaTinta(rendimento, altura, largura):
    area_parede = altura * largura
    cobertura = area_parede / rendimento
    print(f'Você necessita de {cobertura} latas de tinta.')
    
