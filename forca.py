import random

def jogar():

    inicio_do_jogo()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertada = inicializa_letras_acertadas(palavra_secreta) #inicia a palavra secreta

    print(letras_acertada)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto(True and True)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
           marca_chute_correto (palavra_secreta,chute,letras_acertada)
        else:
            erros= erros+1
            print("Ops, você errou! Faltam {} tentativs".format(6-erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertada

        print(letras_acertada)
    if(acertou):
       imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


    print("FIM DO JOGO")

def inicio_do_jogo():
    print("****************************")
    print("BEM VINDO AO JOGO DE FORCA")
    print("****************************")

def carrega_palavra_secreta():
    arquivo = open("arquivo.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra ? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(palavra_secreta,chute,letras_acertada):

    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertada[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("PARABENS... VOCÊ GANHOU O JOGO")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__=="__main__"):
    jogar()









