
from classes_visao.Visao import Visao

class MaoMimica:
    def __init__(self):
        self.visao = Visao()

    def imitar(self):
        while(True):
            try:
                self.printaMenuMaoMimica()

                entradaMaoMimica = int(input())
                print()

                if entradaMaoMimica == 1:
                    print("\nA mão está te imitando! :)")
                    print("Aperte M para a mão parar de te imitar e voltar para o menu da Mão Mímica.")
                    self.visao.visaoImitar()
                    self.imitar()
                elif entradaMaoMimica == 2:
                    print("Voltando para o menu de seleção.")
                    break
                else:
                    print("Opção inválida. Digite 1 ou 2.\n")
            except ValueError:
                print()
                print("Entrada inválida. Digite um número.\n")


    def printaMenuMaoMimica(self):
        print("---------- MÃO MÍMICA ----------")
        print("Insira 1 no terminal para fazer com que a mão te imite;")
        print("Insira 2 no terminal se quer voltar para o menu de seleção.")
        print()
