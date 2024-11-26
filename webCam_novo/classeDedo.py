from classeCoordenada import Coordenada

coordenadaTip = Coordenada("coordenadaTip")
coordenadaIp = Coordenada("coordenadaIp")
coordenadaMcp = Coordenada("coordenadaMcp")
coordenadaCmc = Coordenada("coordenadaCmc")

class Dedo:
    def __init__(self, nome):
        self.nome = nome

        self.distanciaPadraoWristTip = 0.0      #usa a distancia do pulso ate a ponta do dedo como referencia, por isso guardamos a distancia padrao, a anterior e a atual e dos outros dedos nao
        self.distanciaAnteriorWristTip = 0.0

        self.distanciaWristTip = 0.0
        self.distanciaWristIp = 0.0
        self.distanciaWristMcp = 0.0
        self.distanciaWristCmc = 0.0
        
        self.coordenadasPontosDedo = [coordenadaTip, coordenadaIp, coordenadaMcp, coordenadaCmc]
        
        self.tamanhoDivisaoDedo = 0.0