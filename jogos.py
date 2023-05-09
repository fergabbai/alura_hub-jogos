import forca
import advinhacao

def escolha_jogo():

    print("*******************")
    print("Escolha o seu jogo:")
    print("*******************")

    print("(1) Advinhação (2) Forca")

    jogo = int(input("Qual vamos jogar? "))

    if(jogo == 1):
        print("Jogando Advinhação")
        advinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()