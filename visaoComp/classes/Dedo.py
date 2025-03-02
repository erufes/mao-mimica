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


    def determinaDistanciaDedo(self, pontos):
        return pontos[self.landmarkMCP][self.landmarkCMC] - pontos[self.landmarkTIP][self.landmarkCMC]
    
    def setDistanciaDedo(self, distancia):
        self.distancia = distancia

    def setMovimento(self, movimento):
        self.movimento = movimento