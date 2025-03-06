
import random
import serial
import time
import numpy as np

from classes_visao.Visao import Visao

class Jogo:
    def __init__(self):
        # Configuracao da porta serial, que é por onde o arduino vai pegar o arquivo
        self.porta_serial = "/dev/ttyACM0"
        self.baud_rate = 9600

        self.pontuacaoMao = 0
        self.pontuacaoUsuario = 0

        self.pedra = np.array([0, 0, 0, 0, 0])
        self.papel = np.array([4, 4, 4, 4, 4])
        self.tesoura = np.array([0, 4, 4, 0, 0])


    def jogar(self):
        while(True):
            try:
                self.printaMenuJogo()

                entradaJogo = int(input())
                print()

                if entradaJogo == 1:
                    for i in range(3):
                        self.printaComecoJogada(i)
                        
                        visao = Visao()
                        jogadaUsuario = np.array(visao.visaoJogar())
                        jogadaMaoMimica = random.choice([self.pedra, self.papel, self.tesoura])

                        arduino = serial.Serial(self.porta_serial, self.baud_rate)
                        time.sleep(2) 

                        mensagem = f"${''.join(map(str, jogadaMaoMimica))}"
                        print(f"Enviando para Arduino: {mensagem}")

                        # Enviando para o Arduino via Serial
                        arduino.write(mensagem.encode())

                        self.definirQuemPontuou(jogadaMaoMimica, jogadaUsuario)

                    if (self.pontuacaoMao > self.pontuacaoUsuario):
                        print("A Mão Mímica ganhou!")
                    elif (self.pontuacaoMao < self.pontuacaoUsuario):
                        print("O usuário ganhou!")
                    else:
                        print("Empate!")

                    self.pontuacaoMao = 0
                    self.pontuacaoUsuario = 0

                    self.jogar()
                elif entradaJogo == 2:
                    print("Voltando para o menu de seleção.")
                    break
                else:
                    print("Opção inválida. Digite 1 ou 2.\n")
            except ValueError:
                print()
                print("Entrada inválida. Digite um número.\n")


    # Pontua quem ganhou a rodada
    def definirQuemPontuou(self, jogadaMaoMimica, jogadaUsuario):
        jogadaMao = self.retornaJogadaMao(jogadaMaoMimica)
        jogadaUsuarioTratada = self.retornaJogadaUsuario(jogadaUsuario)

        if jogadaUsuarioTratada == jogadaMao:
            print("Empate! Ponto para os dois.")
            self.pontuacaoMao += 1
            self.pontuacaoUsuario += 1
        elif (jogadaUsuarioTratada == 0 and jogadaMao == 2) or \
             (jogadaUsuarioTratada == 1 and jogadaMao == 0) or \
             (jogadaUsuarioTratada == 2 and jogadaMao == 1):
            print("Usuário pontuou!")
            self.pontuacaoUsuario += 1
        else:
            print("Mão Mímica pontuou!")
            self.pontuacaoMao += 1


    # Retorna a qual jogada (pedra, papel ou tesoura) o array da jogada da Mão Mímica se refere
    def retornaJogadaMao(self, jogadaMaoMimica):
        if np.array_equal(jogadaMaoMimica, self.pedra):
            return 0    # Pedra
        elif np.array_equal(jogadaMaoMimica, self.papel):
            return 1    # Papel
        elif np.array_equal(jogadaMaoMimica, self.tesoura):
            return 2    # Tesoura


    # Retorna a qual jogada (pedra, papel ou tesoura) o array da jogada do Usuario se refere
    def retornaJogadaUsuario(self, jogadaUsuario):
        if self.compararComTolerancia(jogadaUsuario, self.pedra):
            return 0  # Pedra
        elif self.compararComTolerancia(jogadaUsuario, self.papel):
            return 1  # Papel
        elif self.compararComTolerancia(jogadaUsuario, self.tesoura):
            return 2  # Tesoura


    # Compara dois arrayas com uma tolerância para margens de erro. Retorna True se os arrays forem "próximos o suficiente"
    def compararComTolerancia(self, array1, array2, tolerancia=2):
        return np.all(np.abs(array1 - array2) <= tolerancia)

    
    # Funções para imprimir no terminal
    def printaComecoJogada(self, i):
        print(f"\nA {i+1}° partida vai começar em...")
        print("3...")
        print("2...")
        print("1!")
        print("Aperte J para fazer sua jogada")

    
    def printaMenuJogo(self):
        print("---------- PEDRA, PAPEL E TESOURA ----------")
        print("Insira 1 no terminal para começar a partida de 3 rodadas;")
        print("Insira 2 no terminal se quer voltar para o menu de seleção.")
        print()
