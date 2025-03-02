import cv2 as openCv
import mediapipe

class Dedo():
    def __init__(self, landmarkMCP, landmarkCMC, landmarkTIP, fechado, 
                 quaseFechado, meioTermo, quaseAberto):
        self.distancia = 0
        self.movimento = 0
        self.landmarkMCP = landmarkMCP
        self.landmarkCMC = landmarkCMC
        self.landmarkTIP = landmarkTIP
        self.fechado = fechado
        self.quaseFechado = quaseFechado
        self.meioTermo = meioTermo
        self.quaseAberto = quaseAberto

    # Calcula a distância do dedo
    def determinaDistanciaDedo(self, pontos):
        return pontos[self.landmarkMCP][self.landmarkCMC] - pontos[self.landmarkTIP][self.landmarkCMC]

    # Funções de determinação
    def setDistanciaDedo(self, distancia):
        self.distancia = distancia

    def setMovimento(self, movimento):
        self.movimento = movimento

    def determinaEstadoDedo(self):
        if self.distancia < self.fechado:
            return 0
        elif self.distancia < self.quaseFechado:
            return 1
        elif self.distancia < self.meioTermo:
            return 2
        elif self.distancia < self.quaseAberto:
            return 3
        else:
            return 4
