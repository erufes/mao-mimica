import cv2 as openCv
import mediapipe

class Dedo():
    def __init__(self):
        self.distancia = 0
        self.movimento = 0

    def determinaDistanciaDedo(pontos, landmark1, landmark2, landmark3):
        return pontos[landmark1][landmark2] - pontos[landmark3][landmark2]
    
    def setDistanciaDedo():
        