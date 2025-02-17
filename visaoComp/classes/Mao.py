import cv2 as openCv
import mediapipe

import Dedo

PULSO = 0
POLEGAR_CMC = 1
POLEGAR_TIP = 4
INDICADOR_MCP = 5
INDICADOR_TIP = 8
MEDIO_MCP = 9 
MEDIO_TIP = 12
ANELAR_MCP = 13
ANELAR_TIP = 16
MINIMO_MCP = 17
MINIMO_TIP = 20

listaLandmarks1 = [                     #a ideia eh deixar menos feio na funcao de determinar a distancia de todos os dedos fazendo um for que percorre as landmarks ao inves de definir uma a uma (nao sei se fica pior sinceramente) 
    17,     # landmark MINIMO_MCP       #usando as listas, essa coisa feia que eh tipo um define nao vai mais precisar ficar ali em cima
    5,      # landmark INDICADOR_MCP
    9,      # landmark MEDIO_MCP
    13,     # landmark ANELAR_MCP
    17,     # landmark MINIMO_MCP
]

listaLandmarks2 = [
    0,      # landmark PULSO
    1,      # landmark POLEGAR_CMC
    1,      # landmark POLEGAR_CMC
    1,      # landmark POLEGAR_CMC
    1,      # landmark POLEGAR_CMC
]

listaLandmarks3 = [
    4,      # landmark POLEGAR_TIP
    8,      # landmark INDICADOR_TIP
    12,     # landmark MEDIO_TIP
    16,     # landmark ANELAR_TIP
    20,     # landmark MINIMO_TIP
]

class Mao():
    def __init__(self):
        self.Dedos = [
            Dedo(),
            Dedo(),
            Dedo(),
            Dedo(),
            Dedo()
        ]

    def determinaDistancia5Dedos(mao, pontos):
        setDistanciaDedo(mao.Dedos[0], abs(determinaDistanciaDedo(pontos, MINIMO_MCP, PULSO, POLEGAR_TIP)))
        setDistanciaDedo(mao.Dedos[1], determinaDistanciaDedo(pontos, MINIMO_MCP, PULSO, POLEGAR_TIP))
        setDistanciaDedo(mao.Dedos[2], determinaDistanciaDedo(pontos, MINIMO_MCP, PULSO, POLEGAR_TIP))
        setDistanciaDedo(mao.Dedos[3], determinaDistanciaDedo(pontos, MINIMO_MCP, PULSO, POLEGAR_TIP))
        setDistanciaDedo(mao.Dedos[4], determinaDistanciaDedo(pontos, MINIMO_MCP, PULSO, POLEGAR_TIP))
        
    