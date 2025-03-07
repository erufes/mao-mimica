
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

class Jogo:
    def __init__(self):
        # Configuracao da porta serial, que é por onde o arduino vai pegar o arquivo
        self.porta_serial = "/dev/ttyACM0"
        self.baud_rate = 9600

        self.pontuacaoMao = 0
        self.pontuacaoUsuario = 0
        self.rodada = 0

        self.pedra = np.array([0, 0, 0, 0, 0])
        self.papel = np.array([4, 4, 4, 4, 4])
        self.tesoura = np.array([0, 4, 4, 0, 0])


    def jogar(self, janela, label, segundos, label_resultado, btn_continuar, btn_iniciar, label_instrucao):
        btn_iniciar.pack_forget()  # Esconde o botão iniciar
        label_instrucao.config(text="")  # Remove "Pronto para iniciar?"
        
        if segundos > 0:
            btn_continuar.pack_forget()
            label.config(text=f"Iniciando em {segundos}...", font=("Arial", 26))
            janela.after(1000, self.jogar, label, segundos - 1, label_resultado, btn_continuar, btn_iniciar, label_instrucao)
        else:
            label.config(text="Captura iniciada!")
            self.rodada(label_resultado, btn_continuar)
            
        if (self.rodada == 3):
            if (self.pontuacaoMao > self.pontuacaoUsuario):
                vencedor = "Usuário"
            elif (self.pontuacaoMao < self.pontuacaoUsuario):
                vencedor = "Mão Mímica"
            else:
                vencedor = "Empate"

            if (vencedor == "Empate"):
                messagebox.showinfo("Fim de Jogo", f"Empate!")
            else:
                messagebox.showinfo("Fim de Jogo", f"{vencedor} venceu a partida!")
            self.pontuacaoMao = 0
            self.pontuacaoUsuario = 0


    def visaoJogar(self):
        camera = openCv.VideoCapture(0)
        camera.set(3,640)
        camera.set(4,480)

        hands = mediapipe.solutions.hands
        Hands = hands.Hands(max_num_hands=1)
        mediapipeDraw = mediapipe.solutions.drawing_utils

        while True:
            success, imagem = camera.read()
            frameRGB = openCv.cvtColor(imagem, openCv.COLOR_BGR2RGB)
            resultados = Hands.process(frameRGB)
            pontosMao = resultados.multi_hand_landmarks
            altura, largura, _ = imagem.shape
            pontos = []
            if pontosMao:
                for points in pontosMao:
                    mediapipeDraw.draw_landmarks(imagem, points, hands.HAND_CONNECTIONS)
                    for id, coordenada in enumerate(points.landmark):
                        coordenadaX, coordenadaY = int(coordenada.x * largura), int(coordenada.y * altura)
                        openCv.circle(imagem, (coordenadaX, coordenadaY), 4, (255,0,0), -1)
                        pontos.append((coordenadaX, coordenadaY))

                    if pontos:
                        mao = Mao(pontos)
                        estadosDedos = mao.analisarDedosMao()
            openCv.imshow('Imagem', imagem)
            key = openCv.waitKey(1) & 0xFF

            if key == ord('j') or key == ord('J') :
                break
        openCv.destroyAllWindows()
        return estadosDedos


    def rodada(self, label_resultado, btn_continuar):
        self.rodada += 1

        messagebox.showinfo("Instrução", "Pressione 'J' para capturar sua jogada.")
            
        jogadaUsuario = np.array(self.visaoJogar())
        jogadaMaoMimica = random.choice([self.pedra, self.papel, self.tesoura])

        arduino = serial.Serial(self.porta_serial, self.baud_rate)
        time.sleep(2) 

        mensagem = f"${''.join(map(str, jogadaMaoMimica))}"

        # Enviando para o Arduino via Serial
        arduino.write(mensagem.encode())

        vencedorRodada = self.definirQuemPontuou(jogadaMaoMimica, jogadaUsuario)

        if (vencedorRodada == "Empate"):
            label_resultado.config(text=f"Rodada concluída!\n\n Empate! O usuário e a mão mímica marcaram ponto\nUsuário: {self.pontuacaoUsuario} | Mão mímica: {self.pontuacaoMao}", font=("Arial", 26))
        else:
            label_resultado.config(text=f"Rodada concluída!\n\n{vencedorRodada} marcou 1 ponto!\nUsuário: {self.pontuacaoUsuario} | Máquina: {self.pontuacaoMao}", font=("Arial", 26))
        btn_continuar.pack(pady=10)


    # Pontua quem ganhou a rodada
    def definirQuemPontuou(self, jogadaMaoMimica, jogadaUsuario):
        jogadaMao = self.retornaJogadaMao(jogadaMaoMimica)
        jogadaUsuarioTratada = self.retornaJogadaUsuario(jogadaUsuario)

        if jogadaUsuarioTratada == jogadaMao:
            self.pontuacaoMao += 1
            self.pontuacaoUsuario += 1
            return "Empate"
        elif (jogadaUsuarioTratada == 0 and jogadaMao == 2) or \
             (jogadaUsuarioTratada == 1 and jogadaMao == 0) or \
             (jogadaUsuarioTratada == 2 and jogadaMao == 1):
            self.pontuacaoUsuario += 1
            return "Usuário"
        else:
            self.pontuacaoMao += 1
            return "Mão mímica"


    # Retorna a qual jogada (pedra, papel ou tesoura) o array da jogada da Mão Mímica se refere
    def retornaJogadaMao(self, jogadaMaoMimica):
        if np.array_equal(jogadaMaoMimica, self.pedra):
            messagebox.showinfo("Mão Mímica jogou Pedra")
            return 0    # Pedra
        elif np.array_equal(jogadaMaoMimica, self.papel):
            messagebox.showinfo("Mão Mímica jogou Papel")
            return 1    # Papel
        elif np.array_equal(jogadaMaoMimica, self.tesoura):
            messagebox.showinfo("Mão Mímica jogou Tesoura")
            return 2    # Tesoura


    # Retorna a qual jogada (pedra, papel ou tesoura) o array da jogada do Usuario se refere
    def retornaJogadaUsuario(self, jogadaUsuario):
        if self.compararComTolerancia(jogadaUsuario, self.pedra):
            messagebox.showinfo("Usuário jogou Pedra")
            return 0  # Pedra
        elif self.compararComTolerancia(jogadaUsuario, self.papel):
            messagebox.showinfo("Usuário jogou Papel")
            return 1  # Papel
        elif self.compararComTolerancia(jogadaUsuario, self.tesoura):
            messagebox.showinfo("Usuário jogou Tesoura")
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
                              command=lambda: self.jogar(self, janela, label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))

        btn_iniciar = tk.Button(frame_inicio, text="Iniciar", font=("Arial", 25), bg="white", fg="black",
                            command=lambda: self.jogar(self, janela, label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))
        btn_iniciar.pack(pady=20)


