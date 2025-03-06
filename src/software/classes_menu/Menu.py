
import cv2 as openCv

import classes_mao.Mao as Mao
import classes_menu.MaoMimica as MaoMimica
import classes_menu.Jogo as Jogo

class Menu:
        def __init__(self, pontos, imagem, openCv):
            self.pontos = pontos
            self.imagem = imagem
            self.openCv = openCv
            self.mao = Mao(pontos)

        def abrirMenu(self):
            print("\n")
            print("---------- MENU ----------\n")
            print("Aperte a tecla 1 se quer que a mão te imite;\n")
            print("Aperte a tecla 2 se quer jogar Pedra, Papel e Tesoura contra a mão;\n")
            print("Aperte a tecla 3 se quer que o programa encerre.\n")

            key = self.openCv.waitKey(0) & 0xFF  # Captura o código ASCII da tecla

            if key == ord('1'):
                print("\nVocê escolheu a Mão Mímica!\n")
                jogo = Jogo(self.mao, self.pontos)
                jogo.jogar(self)
            elif key == ord('2'):
                print("\nVocê escolheu jogar Pedra, Papel e Tesoura!\n")
                maoMimica = MaoMimica(self.mao, self.pontos)
                maoMimica.imitar(self)
            elif key == ord('3'):
                print("\nFechando o programa...\n")
                openCv.destroyAllWindows()
            else:
                print("\nTecla inválida. Tente novamente.\n")
