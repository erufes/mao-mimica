from classeDedo import Dedo
polegar = Dedo("polegar")
indicador = Dedo("indicador")
doMeio = Dedo("meio")
anelar = Dedo("anelar")
mindinho = Dedo("mindinho")
class Mao:
    def __init__(self):
        self.dedos = [polegar, indicador, doMeio, anelar, mindinho]
        self.pontoZeroX = 0.0
        self.pontoZeroY = 0.0
       