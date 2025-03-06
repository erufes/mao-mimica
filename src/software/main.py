
from classes_menu.Jogo import Jogo
from classes_menu.MaoMimica import MaoMimica

def printaMenu():
    print()
    print("---------- MENU ----------")
    print("Insira 1 no terminal se quer que a mão te imite;")
    print("Insira 2 no terminal se quer jogar Pedra, Papel e Tesoura contra a mão;")
    print("Insira 3 no terminal se quer que o programa encerre.\n")

while True:
    try:
        printaMenu()
        
        entradaMenu = int(input())
        print()

        if entradaMenu == 1:
            maoMimica = MaoMimica()
            maoMimica.imitar()
        elif entradaMenu == 2:
            jogo = Jogo()
            jogo.jogar()
        elif entradaMenu == 3:
            print("Encerrando o programa.\n")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")
    except ValueError:
        print()
        print("Entrada inválida. Digite um número.")
