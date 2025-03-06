
import json
import serial
import time

import classes_menu.Menu as Menu

# Configuracao da porta serial, que é por onde o arduino vai pegar o arquivo
porta_serial = "/dev/ttyACM0"

baud_rate = 9600
arduino = serial.Serial(porta_serial, baud_rate)
time.sleep(2) 

class MaoMimica:
    def __init__(self, mao, pontos):
        self.mao = mao

    def imitar(self, menu):
        print("\n")
        print("---------- MAO MÍMICA ----------\n")
        print("Aperte I para fazer com que a mão te imite...\n")
        print("Aperte M se quer voltar para o menu de seleção\n")

        key = self.openCv.waitKey(0) & 0xFF  # Captura o código ASCII da tecla

        if key == ord('I'):
            print("\nA mão está te imitando! :)\n")
            print("Aperte M para a mão parar de te imitar e voltar para o menu de seleção.\n")

            estadosDedos = self.mao.analisarDedosMao()

            mensagem = f"${''.join(map(str, estadosDedos))}"

            # Enviando para o Arduino via Serial
            arduino.write(mensagem.encode())

            with open('estados.json', 'w') as file:
                json.dump({"estados": estadosDedos}, file)
            
            keyMaoMimica = self.openCv.waitKey(0) & 0xFF

            if keyMaoMimica == ord("M"):
                # abre todos os dedos antes de voltar pro menu
                estadosDedos = [4, 4, 4, 4, 4]
                mensagem = f"${''.join(map(str, estadosDedos))}"

                # Enviando para o Arduino via Serial
                arduino.write(mensagem.encode())
                menu.abrirMenu()
        elif key == ord('M'):
            menu.abrirMenu()
        else:
            print("\nTecla inválida. Tente novamente.\n")
