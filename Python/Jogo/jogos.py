import forca
import adivinhacao

print("******************************************")
print("********* ESCOLHA O SEU JOGO! ************")
print("******************************************")

print("(1)Adivinhação (2)Forca")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogo de Adivinhação\n")
    adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
    print("Jogo da Forca\n")
    forca.jogar_forca()
