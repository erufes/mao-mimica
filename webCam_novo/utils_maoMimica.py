import cv2
import math
import mediapipe as mp
import matplotlib.pyplot as plt

from classeDedo import Dedo

def calcularDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia

def xCoordenada(landmark, hand_landmarks, mpHands, image_width):
    return hand_landmarks.landmark[mpHands.HandLandmark(landmark).value].x * image_width
    #return float(str(results.multi_hand_landmarks[-1].landmark[landmark]).split('\n')[0].split(" ")[1])

def yCoordenada(landmark, hand_landmarks, mpHands, image_height):
    return hand_landmarks.landmark[mpHands.HandLandmark(landmark).value].y * image_height
    #return float(str(results.multi_hand_landmarks[-1].landmark[landmark]).split('\n')[1].split(" ")[1])

def DescobrePontosTip(dedo, landmark, hand_landmarks, mpHands, image_width, image_height):
    dedo.pontoTipX = xCoordenada(landmark, hand_landmarks, mpHands, image_width)
    dedo.pontoTipY = yCoordenada(landmark, hand_landmarks, mpHands, image_height)

    return dedo

def DescobrePontosTipDedos(mao, hand_landmarks, mpHands, image_width, image_height):
    for finger in mao.dedos:
        if finger.nome == 'polegar':
            #Descobre o ponto x e y da ponta do polegar
            finger = DescobrePontosTip(finger, 4, hand_landmarks, mpHands, image_width, image_height)
        if finger.nome == 'indicador':
            #Descobre o ponto x e y da ponta do indicador
            finger = DescobrePontosTip(finger, 8, hand_landmarks, mpHands, image_width, image_height)
        if finger.nome == 'meio':
            #Descobre o ponto x e y da ponta do dedo do meio
            mao.doMeio = DescobrePontosTip(finger, 12, hand_landmarks, mpHands, image_width, image_height)
        if finger.nome == 'anelar':
            #Descobre o ponto x e y da ponta do dedo anelar
            mao.anelar = DescobrePontosTip(finger, 16, hand_landmarks, mpHands, image_width, image_height)
        if finger.nome == 'mindinho':   
            #Descobre o ponto x e y da ponta do dedo mindinho
            mao.mindinho = DescobrePontosTip(finger, 20, hand_landmarks, mpHands, image_width, image_height)
    return mao

def CalcularDistanciaAtualDedos(mao):
    for finger in mao.dedos:
        finger.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, finger.pontoTipX, finger.pontoTipY)
    
    return mao

def DefinirDistanciaPadraoDedos(mao):
    for finger in mao.dedos:
        finger.distanciaPadraoZeroTip = finger.distanciaZeroTip
    return mao

def DefinirDistanciaAnteriorDedos(mao):
    for finger in mao.dedos:
        finger.distanciaAnteriorZeroTip = finger.distanciaZeroTip
    return mao

def DescobrePontosDedo(dedo, distanciaPadraoZeroTip):
    dedo.divisaoDedo = distanciaPadraoZeroTip/5
    dedo.distancia1 = distanciaPadraoZeroTip
    dedo.distancia2 = distanciaPadraoZeroTip - dedo.divisaoDedo
    dedo.distancia3 = distanciaPadraoZeroTip - (dedo.divisaoDedo *2)
    dedo.distancia4 = distanciaPadraoZeroTip - (dedo.divisaoDedo *3)
    dedo.distancia5 = distanciaPadraoZeroTip - (dedo.divisaoDedo *4)

    return dedo

def DescobrePontosDedosDivididos(mao):
    for finger in mao.dedos:
        finger = DescobrePontosDedo(finger, finger.distanciaPadraoZeroTip)
    return mao
           
            
