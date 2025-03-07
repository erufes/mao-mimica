
import tkinter as tk
import cv2 as openCv
import time
import serial
import mediapipe
from tkinter import messagebox

from classes_visao.Visao import Visao

class MaoMimica:
    def __init__(self):
        self.visao = Visao()

    def imitar(self):
        while(True):
            try:
                messagebox.showinfo("Instrução", "Movimente sua mão para enviar comandos ao Arduino.\nPressione 'E' para encerrar.")

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
