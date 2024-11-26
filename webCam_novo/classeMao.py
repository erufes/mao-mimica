from classeDedo import Dedo
from classeCoordenada import Coordenada

coordenadaWrist = Coordenada("coordenadaWrist")

thumb = Dedo("thumb")
index = Dedo("index")
middle = Dedo("middle")
ring = Dedo("ring")
pinky = Dedo("pinky")

class Mao:
    def __init__(self):
        self.dedos = [thumb, index, middle, ring, pinky]
        self.coordenadaWrist = coordenadaWrist
       