import cv2
import math
import mediapipe as mp
import matplotlib.pyplot as plt

from classeDedo import Dedo

class Utils:
    def __init__(self):
            
        #Funcao para calcular a distancia entre dois pontos de uma imagem 2d
        def calcularDistancia(x1, y1, x2, y2):
            distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            return distancia

        #Funcao para descobrirmos a coordenada x de um ponto do dedo que especificarmos
        def xCoordenada(landmark, results):
            #return hand_landmarks.landmark[mpHands.HandLandmark(landmark).value].x * image_width
            return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split('\n')[0].split(" ")[1])

        #Funcao para descobrirmos a coordenada y de um ponto do dedo que especificarmos
        def yCoordenada(landmark, results):
            #return hand_landmarks.landmark[mpHands.HandLandmark(landmark).value].y * image_height
            return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split('\n')[1].split(" ")[1])
    
        def DescobrePontosTip(landmark, results):
            dedo = Dedo()
            dedo.pontoTipX = xCoordenada(landmark, results)
            dedo.pontoTipY = yCoordenada(landmark, results)

            return dedo

        def DescobrePontosTipDedos(mao, results):
            #Descobre o ponto x e y da ponta do polegar
            mao.polegar = DescobrePontosTip(4, results)

            #Descobre o ponto x e y da ponta do indicador
            mao.indicador = DescobrePontosTip(8, results)

            #Descobre o ponto x e y da ponta do dedo do meio
            mao.doMeio = DescobrePontosTip(12, results)

            #Descobre o ponto x e y da ponta do dedo anelar
            mao.anelar = DescobrePontosTip(16, results)

            #Descobre o ponto x e y da ponta do dedo mindinho
            mao.mindinho = DescobrePontosTip(20, results)

        def CalcularDistanciaAtualDedos(mao):
            mao.polegar.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.polegar.pontoTipX, mao.polegar.pontoTipY)
            mao.indicador.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.indicador.pontoTipX, mao.indicador.pontoTipY)
            mao.doMeio.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.doMeio.pontoTipX, mao.doMeio.pontoTipY)
            mao.anelar.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.anelar.pontoTipX, mao.anelar.pontoTipY)
            mao.mindinho.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.mindinho.pontoTipX, mao.mindinho.pontoTipY)

            return mao

        def DefinirDistanciaPadraoDedos(mao):
            mao.polegar.distanciaPadraoZeroTip = mao.polegar.distanciaZeroTip
            mao.indicador.distanciaPadraoZeroTip = mao.indicador.distanciaZeroTip
            mao.doMeio.distanciaPadraoZeroTip = mao.doMeio.distanciaZeroTip
            mao.anelar.distanciaPadraoZeroTip = mao.anelar.distanciaZeroTip
            mao.mindinho.distanciaPadraoZeroTip = mao.mindinho.distanciaZeroTip

            return mao
        
        def DefinirDistanciaAnteriorDedos(mao):
            mao.polegar.distanciaAnteriorZeroTip = mao.polegar.distanciaZeroTip
            mao.indicador.distanciaAnteriorZeroTip = mao.indicador.distanciaZeroTip
            mao.doMeio.distanciaAnteriorZeroTip = mao.doMeio.distanciaZeroTip
            mao.anelar.distanciaAnteriorZeroTip = mao.anelar.distanciaZeroTip
            mao.mindinho.distanciaAnteriorZeroTip = mao.mindinho.distanciaZeroTip

            return mao
        
        def DescobrePontosDedo(dedo, distanciaPadraoZeroTip):
            dedo.divisaoDedo = distanciaPadraoZeroTip/5
            dedo.distancia1 = distanciaPadraoZeroTip
            dedo.distancia2 = distanciaPadraoZeroTip - dedo.DivisaoDedo
            dedo.distancia3 = distanciaPadraoZeroTip - (dedo.divisaoDedo *2)
            dedo.distancia4 = distanciaPadraoZeroTip - (dedo.divisaoDedo *3)
            dedo.distancia5 = distanciaPadraoZeroTip - (dedo.divisaoDedo *4)

            return dedo

        def DescobrePontosDedosDivididos(mao):
            mao.polegar = DescobrePontosDedo(mao.polegar, mao.polegar.distanciaPadraoZeroTip)
            mao.indicador = DescobrePontosDedo(mao.indicador.distanciaPadraoZeroTip)
            mao.doMeio = DescobrePontosDedo(mao.doMeio.distanciaPadraoZeroTip)
            mao.anelar = DescobrePontosDedo(mao.anelar.distanciaPadraoZeroTip)
            mao.mindinho = DescobrePontosDedo(mao.mindinho.distanciaPadraoZeroTip)

            return mao
