import random

def jogar():

    print("*******************************")
    print("Bem-vindo ao Jogo de Advinhação!")
    print("*******************************")

    numero_secreto = round(random.randrange(1,11))
    tentativas = 0
    pontos = 100

    print("Níveis:")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha seu nível: "))

    if(nivel == 1):
        tentativas = 7
    elif(nivel == 2):
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um palpite entre 1 e 10: "))
        print("Seu palpite é", chute)

        if(chute < 1 or chute > 50):
            print("Seu palpite deve ser entre 1 e 10")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("VOCÊ ACERTOU e fez {} pontos!!!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O número secreto é MENOR.")
            elif(menor):
                print("Você errou! O número secreto é MAIOR.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("FIM DE JOGO!")

if(__name__ == "__main__"):
    jogar()