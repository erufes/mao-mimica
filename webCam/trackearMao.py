import cv2
import math
import json
import mediapipe as mp
import matplotlib.pyplot as plt

from utils_maoMimica import Utils
from classeMao import Mao
from classeDedo import Dedo
movements = []
mpDrawing = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

#Funcao para o Open CV capturar o video pela camera conectada no USB
cap = cv2.VideoCapture(1)
cap.set(3, 720)  # Define a largura do frame
cap.set(4, 480)  # Define a altura do frame

frame_width = 720
frame_heigth = 480

#Inicia a mao inteira, classe que tem o ponto zero da mao e os dedos
mao = Mao()
#Inicia as funcoes utils_maoMimica
utils = Utils()

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
    if k == ord('q') or k == ord('Q') or k == 27:
        exit(1)

    elif (k == ord('t')):
        while True:
            k = cv2.waitKey(10)
            if k == ord('q') or k == ord('Q') or k == 27:
                exit(1)
            
            #Agora, setamos o hands para usar uma imagem estatica
            hands = mpHands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

            #Tiramos foto da mao
            cv2.imwrite("fotoMao.png", image)
            maoImagem = cv2.imread("fotoMao.png")
            plt.figure(figsize = [10, 10])

            results = hands.process(cv2.cvtColor(maoImagem, cv2.COLOR_BGR2RGB))
            
            if results.multi_hand_landmarks:
                for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    
                    mpDrawing.draw_landmarks(image = maoImagem, landmark_list = hand_landmarks,
                                            connections = mpHands.HAND_CONNECTIONS)
                fig = plt.figure(figsize = [10, 10])

            image_height, image_width = maoImagem.shape

            #Esse jeito de descobrir a coordenada x e y de cada ponto da mao converte para os centimetros do tamanho da foto 
            mao.pontoZeroX = hand_landmarks.landmark[mpHands.HandLandmark(0).value].x *frame_width
            mao.pontoZeroY = hand_landmarks.landmark[mpHands.HandLandmark(0).value].y *frame_heigth
            
            mao = utils.DescobrePontosTipDedos(mao, results)

            mao = utils.CalcularDistanciaAtualDedos(mao)

            mao = utils.DefinirDistanciaPadraoDedos(mao)

            mao = utils.DefinirDistanciaAnteriorDedos(mao)

            mao = utils.DescobrePontosDedosDivididos(mao)

            while True:
                hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
                image = cap.read()
                results = hands.process(image)

                mao.pontoZeroX = hand_landmarks.landmark[mpHands.HandLandmark(0).value].x *image_width
                mao.pontoZeroY = hand_landmarks.landmark[mpHands.HandLandmark(0).value].y *image_height

                mao = utils.DescobrePontosTipDedos(mao, results)

                mao = utils.CalcularDistanciaAtualDedos(mao)

                for finger in mao.dedos:
                #Se identificar que a distancia padrao esta maior que a calculada, quer dizer que a pessoa baixou o dedo
                    if (finger.distanciaAnteriorZeroTip > finger.distanciaZeroTip):
                        if (finger.distanciaZeroTip == finger.distancia2):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia1):
                                #baixar 36 graus 1 vez
                                movement = {finger.nome: "abaixar 1 bloco"}
                                movements.append(movement)
                        elif (finger.distanciaZeroTip == finger.distancia3):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia1):
                                #baixar 36 graus 2 vezes
                                movement = {finger.nome: "abaixar 2 blocos"}
                                movements.append(movement)
                            elif(finger.distanciaAnteriorZeroTip == finger.distancia2):
                                #baixar 36 graus 1 vez
                                movement = {finger.nome: "abaixar 1 bloco"}
                                movements.append(movement)
                    elif (finger.distanciaAnteriorZeroTip < finger.distanciaZeroTip):
                        if (finger.distanciaZeroTip == finger.distancia1):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia2):
                                #subir 36 graus 1 vez
                                movement = {finger.nome: "subir 1 bloco"}
                                movements.append(movement)
                            elif (finger.distanciaAnterior.ZeroTip == finger.distancia3):
                                #subir 36 graus 2 vezes
                                movement = {finger.nome: "subir 2 blocos"}
                                movements.append(movement)
                        elif (finger.distanciaZeroTip == finger.distancia2):
                            if (finger.distanciaAnteriorZeroTip == finger.distancia3):
                                #subir 36 graus 1 vez
                                movement = {finger.nome: "subir 1 bloco"}
                                movements.append(movement)
                            elif (finger.distanciaAnteriorZeroTip == finger.distancia4):
                                #subir 36 graus 2 vezes
                                movement = {finger.nome: "subir 2 blocos"}
                                movements.append(movement)
                                
                    with open("movements.json", "a") as json_file: 
                        json.dump(movements, json_file, indent = 4)
                    
                mao = utils.DefinirDistanciaAnteriorDedos(mao)

                k = cv2.waitKey(10)
                if k == ord('q') or k == ord('Q') or k == 27:
                    exit(1)
                elif (k == ord('t')):
                    break
cap.release()