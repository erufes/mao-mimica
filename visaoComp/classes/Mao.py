import cv2 as openCv
import mediapipe

import Dedo

LANDMARKS_MCP = [17, 5, 9, 13, 17]      # Polegar, Indicador, Médio, Anelar, Mínimo
LANDMARKS_CMC = [0, 1, 2, 3, 4]         # Polegar, Indicador, Médio, Anelar, Mínimo
LANDMARKS_TIP = [4, 8, 12, 16, 20]      # Polegar, Indicador, Médio, Anelar, Mínimo

DISTANCIAS_FECHADO = [70, 10, -10, -20, 0]          # Polegar, Indicador, Médio, Anelar, Mínimo
DISTANCIAS_QUASE_FECHADO = [100, 50, 10, 10, 30]
DISTANCIAS_MEIO_TERMO = [140, 80, 60, 60, 50]
DISTANCIAS_QUASE_ABERTO = [180, 100, 110, 110, 70]

class Mao:
    def __init__(self):
        self.Dedos = [
            Dedo(LANDMARKS_MCP[i], LANDMARKS_CMC[i], LANDMARKS_TIP[i], 
                 DISTANCIAS_FECHADO[i], DISTANCIAS_QUASE_FECHADO[i], 
                 DISTANCIAS_MEIO_TERMO[i], DISTANCIAS_QUASE_ABERTO[i])
            for i in range(5) 
        ]

    def determinaDistancia5Dedos(self, pontos):
        for dedo in range(5):
            if dedo == 0:
                Dedo.setDistanciaDedo(self.Dedos[dedo], abs(Dedo.determinaDistanciaDedo(self.Dedos[dedo], pontos)))
            else:
                Dedo.setDistanciaDedo(self.Dedos[dedo], Dedo.determinaDistanciaDedo(self.Dedos[dedo], pontos))

    def analisarDedosMao(self, pontos):
