# Ponto da carne de churrasco
# A partir da temperatura do termometro ver qual o ponto da carne 
# Temperatura de cozimento
#   Antes de 48°C - Cozinhar por mais alguns minutos
#   120°F ou 48°C - Rare (Selada)
#   130°F ou 54°C - Medium rare (Ao ponto para o mal)
#   140°F ou 60°C - Medium(Ao ponto)
#   150°F ou 65°C - Medium well (Ao ponto para o bem)
#   160°F ou 71°C - Well Done (Bem passada)
#   Passou dos 71°C bem passada


temp_Carne = int(input('Qual a temperatura da carne? '))


if (temp_Carne < 48):
    print('Cozinhar por mais alguns minutos.')
elif(temp_Carne >= 48 and temp_Carne < 54):
    print('A carne está selada')
elif(temp_Carne >= 54 and temp_Carne < 60):
    print('A carme está ao ponto para mal passada')
elif(temp_Carne >= 60 and temp_Carne < 65):
    print('A Carne está ao ponto')
elif(temp_Carne >= 65 and temp_Carne < 71):
    print('A carme está ao ponto para bem passada')
elif(temp_Carne >= 71 and temp_Carne < 80):
    print('A carme está bem passada')
else:
    print('CARVÃO')


