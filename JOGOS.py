import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("ESCOLHA O JOGO QUE QUER JOGAR")
    print("*********************************")


    print("(1) Forca (2) Adivinhação")

    jogo=int(input("Qual jogo você quer jogar? "))

    if(jogo ==1):
        print("JOGO DO FORCA")
        forca.jogar()
    elif(jogo==2):
        print("JOGO DA ADIVINHAÇÃO")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolha_jogo()










