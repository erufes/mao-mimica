
from classes_visao.Visao import Visao

class MaoMimica:
    def __init__(self):
        self.mao = any

    def imitar(self):
        print("\n")
        print("---------- MAO MÍMICA ----------")
        print("Insira 1 no terminal para fazer com que a mão te imite;")
        print("Insira 2 no terminal se quer voltar para o menu de seleção.")

        while(True):
            try:
                entradaMaoMimica = int(input())

                if entradaMaoMimica == 1:
                    print("\nA mão está te imitando! :)")
                    print("Aperte M para a mão parar de te imitar e voltar para o menu da Mão Mímica.")
                    visao = Visao()
                    visao.visaoImitar()
                    self.imitar()
                elif entradaMaoMimica == 2:
                    print("Voltando para o menu de seleção.")
                    break
                else:
                    print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Digite um número")
