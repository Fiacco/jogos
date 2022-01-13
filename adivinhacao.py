import random

def jogar():
    print("*********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("*********************************")

    numero_secreto =random.randrange(1,101) # importei essa função para gerar um numero aleatorio numero_secreto" é uma variavel
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha um nivel de dificuldade:")
    print("(1)FÁCIL (2) MÉDIO (3) DIFÍCIL")

    nivel = int(input("Defina um nivel : "))

    if(nivel ==1):
        total_de_tentativas = 15
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100 ):
            print("Você tem que digitar um numero de 1 a 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! o numero secreto é menor \n")
            elif(menor):
                print("Você errou! o numero secreto é maior \n")
            pontos_perdidos = abs(numero_secreto - chute) # toda vez que chutar vai tirar os pontos com o valor do chute caso erre por exempo = 40 - 20 = 20
            pontos = pontos - pontos_perdidos

    print("FIM DO JOGO")

if(__name__ == "__main__"):
    jogar()










