
import tkinter as tk
import cv2 as openCv
import time
import serial
import mediapipe
from classes_mao.Mao import Mao
from classes_mao.Dedo import Dedo
from tkinter import messagebox

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


    def jogar(self, janela):
        while(True):
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
                    #print(f"Enviando para Arduino: {mensagem}")

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

    
    # 
    def menuJogo(self, janela):
        for widget in janela.winfo_children():
                    widget.destroy()

        frame_inicio = tk.Frame(janela, bg="#FFC0CB")
        frame_inicio.place(relx=0.5, rely=0.5, anchor="center")

        label_instrucao = tk.Label(frame_inicio, text="Pronto para iniciar?", font=("Arial", 36), bg="#FFC0CB")
        label_instrucao.pack(pady=5)

        label_resultado = tk.Label(frame_inicio, text="", font=("Arial", 22), bg="#FFC0CB")
        label_resultado.pack(pady=5)

        btn_continuar = tk.Button(frame_inicio, text="Continuar", font=("Arial", 22), bg="white", fg="black",
                              command=lambda: self.jogar(label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))

        btn_iniciar = tk.Button(frame_inicio, text="Iniciar", font=("Arial", 25), bg="white", fg="black",
                            command=lambda: self.jogar(label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))
        btn_iniciar.pack(pady=20)


