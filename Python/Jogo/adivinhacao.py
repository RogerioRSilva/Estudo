import random

def jogar_adivinhacao():
    print("******************************************")
    print("Bem vindo ao Jogo de Adivinhação!")
    print("******************************************")

    numero_secreto = random.randrange(1, 101) # Começa no 1  até 100 pois o 101 e 0 são ignorados.
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1)Fácil  (2)Médio  (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print(f'Tentativas {rodada} de {total_de_tentativas}:')
        rodada += 1

        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!!!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f"Você Acertou!!! Fez {pontos} pontos.")
            break
        else:
            if (maior):
                print("Você Errou!!! Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Você Errou!!! Seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute) # Função abs é usada para tornar um numero absoluto ou seja não tem negativo.
            pontos = pontos - pontos_perdidos


    print("\n<<<<< FIM DO JOGO >>>>>")

if (__name__ == "__main__"):
    jogar_adivinhacao()