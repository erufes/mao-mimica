
import Dedo

# Array que guarda o estado de cada dedo
# 0 = totalmente fechado
# 1 = quase totalmente fechado
# 2 = meio termo
# 3 = quase totalmente aberto
# 4 = totalmente aberto
estadosDedos = [4, 4, 4, 4, 4]      # Deixa todos os dedos em estado totalmente aberto


# Cada posição dos arrays corresponde a um dedo         # Polegar:          Indicador:          Médio:          Anelar:         Mínimo:
LANDMARKS_MCP = [17, 5, 9, 13, 17]                      # MINIMO_MCP        INDICADOR_MCP       MEDIO_MCP       ANELAR_MCP      MINIMO_MCP 
LANDMARKS_CMC = [0, 1, 1, 1, 1]                         # PULSO             POLEGAR_CMC         POLEGAR_CMC     POLEGAR_CMC     POLEGAR_CMC
LANDMARKS_TIP = [4, 8, 12, 16, 20]                      # MINIMO_TIP        INDICADOR_TIP       MEDIO_TIP       ANELAR_TIP      MINIMO_TIP

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
            for i in range(5)       # O i corresponde a um dedo, por exemplo se i==0 então corresponde ao polegar, assim definindo todas as constantes de cada dedo
        ]

    # Percorre todos os dedos para definir a distancia calculada 
    def determinaDistancia5Dedos(self, pontos):     
        for dedo in range(5):
            if dedo == 0:       # Se for o polegar
                Dedo.setDistanciaDedo(self.Dedos[dedo], abs(Dedo.determinaDistanciaDedo(self.Dedos[dedo], pontos)))
            else:
                Dedo.setDistanciaDedo(self.Dedos[dedo], Dedo.determinaDistanciaDedo(self.Dedos[dedo], pontos))

    # Analisa o estado de cada dedo da mão
    def analisarDedosMao(self, pontos):
        self.determinaDistancia5Dedos(self, pontos)
        
        for dedo in range(5):
            estadosDedos[dedo] = Dedo.determinaEstadoDedo(self.Dedos[dedo])
        return estadosDedos