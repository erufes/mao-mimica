
from classes_mao.Mao import Mao
from classes_mao.Dedo import Dedo
from classes_menu.Jogo import Jogo
from classes_menu.MaoMimica import MaoMimica

print("\n")
print("---------- MENU ----------\n")
print("Insira 1 no terminal se quer que a mão te imite;\n")
print("Insira 2 no terminal se quer jogar Pedra, Papel e Tesoura contra a mão;\n")
print("Insira 3 no terminal se quer que o programa encerre.\n")

while True:
    try:
        entradaMenu = int(input())

        if entradaMenu == 1:
            print("Iniciando modo mão mímica...\n")
            maoMimica = MaoMimica()
            maoMimica.imitar()
        elif entradaMenu == 2:
            print("Iniciando Pedra, Papel e Tesoura...\n")
            jogo = Jogo()
            jogo.jogar()
        elif entradaMenu == 3:
            print("Encerrando o programa.\n")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.\n")
    except ValueError:
        print("Entrada inválida. Digite um número.\n")
