
import random
import serial
import time

from classes_visao.Visao import Visao

class Jogo:
    def __init__(self):
        self.mao = any
        self.pontuacaoMao = 0
        self.pontuacaoUsuario = 0
        self.rodadas = 0
        self.pedra = [0, 0, 0, 0, 0]
        self.papel = [4, 4, 4, 4, 4]
        self.tesoura = [0, 4, 4, 0, 0]

    def jogar(self):
        print("\n")
        print("---------- PEDRA, PAPEL OU TESOURA ----------")
        print("Insira 1 no terminal para começar a partida de 3 rodadas;")
        print("Insira 2 no terminal se quer voltar para o menu de seleção.")

        while(True):
            try:
                entradaJogo = int(input())

                if entradaJogo == 1:
                    print("\aA partida vai começar em...")
                    print("3...")
                    print("2...")
                    print("1!")
                    print("Aperte J para fazer sua jogada")
                    
                    visao = Visao()
                    jogadaUsuario = visao.visaoJogar()
                    jogadaMaoMimica = random.choice([self.pedra, self.papel, self.tesoura])

                    # Configuracao da porta serial, que é por onde o arduino vai pegar o arquivo
                    porta_serial = "/dev/ttyACM0"

                    baud_rate = 9600
                    arduino = serial.Serial(porta_serial, baud_rate)
                    time.sleep(2) 

                    mensagem = f"${''.join(map(str, jogadaMaoMimica))}"
                    print(f"Enviando para Arduino: {mensagem}")

                    # Enviando para o Arduino via Serial
                    arduino.write(mensagem.encode())
                    
                    #chamar a funcao de visao que identifica o que a pessoa jogou e recebe um array 
                    #fazer a mao mimica escolher um random entre 3 arrays, que sao a possibilidade de jogada
                    #comparar o array recebido com as possibilidades de jogada, identificar o que a pessoa jogou e comparar com a jogada do robo
                    #dependendo da jogada, ele printa quem pontuou

                    print("Se prepare para sua pŕoxima jogada em...")
                    print("3...")
                    print("2...")
                    print("1!")
                    print("Aperte J para fazer sua jogada")

                    #faz a mesma coisa de antes

                    print("Se prepare para sua última jogada em...")
                    print("3...")
                    print("2...")
                    print("1...")
                    print("Aperte J para fazer sua jogada")

                    # agora compara e ve quem ganhou
                    self.jogar()
                elif entradaJogo == 2:
                    print("Voltando para o menu de seleção.")
                    break
                else:
                    print("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Digite um número")
