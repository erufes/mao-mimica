
import tkinter as tk
import cv2
import time
from tkinter import messagebox

from classes_menu.Menu import Menu


menu = Menu()

# Criando a janela principal
janela = tk.Tk()
janela.title("Jogo de Detecção de Mãos")
janela.attributes('-fullscreen', True)  # Ocupa a tela inteira
janela.configure(bg="#FFC0CB")

# Exibe o menu ao iniciar
menu.mostrarMenu(janela)

# Rodando a interface
janela.mainloop()
