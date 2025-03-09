

import tkinter as tk
import cv2
import time
from tkinter import messagebox

from classes_menu.Jogo import Jogo
from classes_menu.MaoMimica import MaoMimica

class Menu:
    def __init__(self):
        self.mao = MaoMimica()
        self.jogo = Jogo(self)

    def mostrarMenu(self, janela):
        for widget in janela.winfo_children():
                widget.destroy()

        # Criando um frame central para agrupar os elementos
        frame_menu = tk.Frame(janela, bg="#FFC0CB")
        frame_menu.place(relx=0.5, rely=0.45, anchor="center")  # Centraliza no meio da tela

        # Título do menu
        label_titulo = tk.Label(frame_menu, text="Mão Mímica", font=("Arial", 40), bg="#FFC0CB")
        label_titulo.pack(pady=20)  # Pequeno espaçamento abaixo do título

        # Botão "Imitar movimentos da mão"
        btn_imitar = tk.Button(frame_menu, text="Imitar movimentos da mão", command=self.mao.imitar, 
                            width=25, font=("Arial", 22), bg="white", fg="black")
        btn_imitar.pack(pady=15)  # Espaçamento entre os botões

        # Botão "Jogar Pedra, Papel e Tesoura"
        btn_jogar = tk.Button(frame_menu, text="Jogar Pedra, Papel e Tesoura", command=lambda: self.jogo.menuJogo(janela), 
                            width=25, font=("Arial", 22), bg="white", fg="black")
        btn_jogar.pack(pady=15)

        # Botão "Encerrar programa"
        btn_encerrar = tk.Button(frame_menu, text="Encerrar programa", command=janela.quit, 
                            width=25, font=("Arial", 22), bg="red", fg="white")
        btn_encerrar.pack(pady=15)
