import cv2
import json
import mediapipe as mp
import matplotlib.pyplot as plt

import utils_maoMimica as utils
from classeMao import Mao
from classeDedo import Dedo

movements = {
}

mpDrawing = mp.solutions.drawing_utils
mpHands = mp.solutions.hands

sentidoHorario = 0      #saber se o motor deve rodar sentido horario (para fechar a mao) pu sentido anti-horario (para abrir a mao)
qtdMovimentos = 0       #quantas vezes devemos girar tantos graus do motor para a mao abrir ou fechar ate o lugar certo

hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
handsImage = mpHands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Funcao para o Open CV capturar o video pela camera conectada no USB
cap = cv2.VideoCapture(0)
cap.set(3, 720)  # Define a largura do frame
cap.set(4, 480)  # Define a altura do frame

frame_width = 720
frame_heigth = 480

#Inicia a mao inteira, classe que tem a coordenada wrist da mao e os dedos
mao = Mao()

while cap.isOpened():
    sucess, image = cap.read()

    if not sucess:
        print("Ignoring empty camera frame.")
        continue

    #Flip the image horizontally for a later selfie-view display, and convert
    #the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    #To improve performance, optionally mark the image as not writeable to
    #pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    #Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mpDrawing.draw_landmarks(
                image, hand_landmarks, mpHands.HAND_CONNECTIONS)
            
    cv2.imshow("MediaPipe Hands", image)

    k = cv2.waitKey(10)
    if k == ord('q') or k == ord('Q') or k == 27:   #para fechar o programa
        exit(1)

    elif (k == ord('t') or k == ord('T')):  #para tirar foto da mao que servira como modelo de analise       
        while True:
            if k == ord('q') or k == ord('Q') or k == 27:   #para fechar o programa
                exit(1)
                
            cv2.imwrite("fotoMao.png", image)
            maoImagem = cv2.imread("fotoMao.png")
            plt.figure(figsize = [10, 10])

            resultsImage = handsImage.process(cv2.cvtColor(maoImagem, cv2.COLOR_BGR2RGB))
            
            if resultsImage.multi_hand_landmarks:
                for hand_no, hand_landmarks in enumerate(resultsImage.multi_hand_landmarks):
                    
                    mpDrawing.draw_landmarks(image = maoImagem, landmark_list = hand_landmarks,
                                            connections = mpHands.HAND_CONNECTIONS)
                fig = plt.figure(figsize = [10, 10])

            image_width = maoImagem.shape[1]
            image_height = maoImagem.shape[0]

            #Esse jeito de descobrir a coordenada x e y de cada ponto da mao converte para os centimetros do tamanho da foto 
            mao.coordenadaWrist.x = hand_landmarks.landmark[mpHands.HandLandmark(0).value].x *frame_width
            mao.coordenadaWrist.y = hand_landmarks.landmark[mpHands.HandLandmark(0).value].y *frame_heigth
            
            mao = utils.DescobrePontosTipDedos(mao, hand_landmarks, mpHands, image_width, image_height)

            mao = utils.CalcularDistanciaAtualDedos(mao)

            mao = utils.DefinirDistanciaPadraoDedos(mao)

            mao = utils.DefinirDistanciaAnteriorDedos(mao)

            mao = utils.DescobrePontosDedosDivididos(mao)

            while True:
                mao.pontoZeroX = hand_landmarks.landmark[mpHands.HandLandmark(0).value].x *image_width
                mao.pontoZeroY = hand_landmarks.landmark[mpHands.HandLandmark(0).value].y *image_height

                mao = utils.DescobrePontosTipDedos(mao, hand_landmarks, mpHands, image_width, image_height)

                mao = utils.CalcularDistanciaAtualDedos(mao)

                i = 0
                for finger in mao.dedos:
                #Se identificar que a distancia padrao esta maior que a calculada, quer dizer que a pessoa baixou o dedo
                    if (finger.distanciaAnteriorZeroTip > finger.distanciaZeroTip):
                        cimaBaixo = 0
                        if (finger.distanciaZeroTip == finger.distancia2):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia1):
                                #baixar 36 graus 1 vez
                                qtdMovimentos = 1
                        elif (finger.distanciaZeroTip == finger.distancia3):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia1):
                                #baixar 36 graus 2 vezes
                                qtdMovimentos = 2
                            elif(finger.distanciaAnteriorZeroTip == finger.distancia2):
                                #baixar 36 graus 1 vez
                                qtdMovimentos = 1
                    elif (finger.distanciaAnteriorZeroTip < finger.distanciaZeroTip):
                        cimaBaixo = 1
                        if (finger.distanciaZeroTip == finger.distancia1):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia2):
                                #subir 36 graus 1 vez
                                qtdMovimentos = 1
                            elif (finger.distanciaAnterior.ZeroTip == finger.distancia3):
                                #subir 36 graus 2 vezes
                                qtdMovimentos = 2
                        elif (finger.distanciaZeroTip == finger.distancia2):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia3):
                                #subir 36 graus 1 vez
                                qtdMovimentos = 1
                            elif (finger.distanciaAnteriorZeroTip == finger.distancia4):
                                #subir 36 graus 2 vezes
                                qtdMovimentos = 2
                    else:
                        cimaBaixo = 0
                        qtdMovimentos = 0

                    movements[finger.nome] = [cimaBaixo, qtdMovimentos]
                    i = i+1
        
                with open("movements.json", "w") as json_file: 
                    json.dump(movements, json_file, indent = 2)
                    
                mao = utils.DefinirDistanciaAnteriorDedos(mao)

                k = cv2.waitKey(10)
                if k == ord('q') or k == ord('Q') or k == 27:
                    exit(1)
                elif (k == ord('t')):
                    break
cap.release()