
import tkinter as tk
import cv2
import time
from tkinter import messagebox

from classes_menu.Jogo import Jogo
from classes_menu.MaoMimica import MaoMimica


def mostrarMenu(janela):
    for widget in janela.winfo_children():
            widget.destroy()

    # Criando um frame central para agrupar os elementos
    frame_menu = tk.Frame(janela, bg="#FFC0CB")
    frame_menu.place(relx=0.5, rely=0.45, anchor="center")  # Centraliza no meio da tela

    # Título do menu
    label_titulo = tk.Label(frame_menu, text="Menu Mão Mímica", font=("Arial", 40), bg="#FFC0CB")
    label_titulo.pack(pady=20)  # Pequeno espaçamento abaixo do título

    # Botão "Imitar movimentos da mão"
    btn_imitar = tk.Button(frame_menu, text="Imitar movimentos da mão", command=maoMimica.imitar, 
                        width=25, font=("Arial", 22), bg="white", fg="black")
    btn_imitar.pack(pady=15)  # Espaçamento entre os botões

    # Botão "Jogar Pedra, Papel e Tesoura"
    btn_jogar = tk.Button(frame_menu, text="Jogar Pedra, Papel e Tesoura", command=jogo.jogar, 
                        width=25, font=("Arial", 22), bg="white", fg="black")
    btn_jogar.pack(pady=15)

    # Botão "Encerrar programa"
    btn_encerrar = tk.Button(frame_menu, text="Encerrar programa", command=janela.quit, 
                        width=25, font=("Arial", 22), bg="red", fg="white")
    btn_encerrar.pack(pady=15)


jogo = Jogo()
maoMimica = MaoMimica()

# Criando a janela principal
janela = tk.Tk()
janela.title("Jogo de Detecção de Mãos")
janela.attributes('-fullscreen', True)  # Ocupa a tela inteira
janela.configure(bg="#FFC0CB")

# Exibe o menu ao iniciar
mostrarMenu()

# Rodando a interface
janela.mainloop()