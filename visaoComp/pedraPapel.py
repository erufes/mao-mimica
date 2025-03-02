
class Jogo:
    def __init__(self, mao, pontos):
        self.mao = mao
        self.pontuacaoMao = 0
        self.pontuacaoUsuario = 0
        self.rodadas = 0

    def jogar(self):
        print("\n")
        print("---------- PEDRA, PAPEL OU TESOURA ----------\n")
        print("Aperte J para começar a partida de 3 rodadas...\n")

        # esqueci como que bota pra esperar clicar a tecla rs
        # ai quando apertar ele faz um timer de 3 2 1 

        # ai chama random jogada e identificar jogada
        # se o array dos dois for igual, adiciona 1 ponto na pontuacao dos dois
        # se o array da mao ganha do array do usuario, adc 1 ponto na pontuacao da mao

        # assim vai até ter 3 rodadas
        # mostra quem ganhou e mostra se deseja jogar outra partida, ir para o menu ou encerrar o programa
        
        # se escolher jogar outra partida, reinicia tudo


    def identificarJogada(self):
        # ele recebe o array com os estados da mao e analisa qual foi jogada

    def randomJogada(self):
        # um random entre os 3 arrays possiveis é feito e a mao executa um deles mandando por serial (igual quando imita mesmo)
