import cv2
import math
import mediapipe as mp
import matplotlib.pyplot as plt

mpDrawing = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

class Dedo:
    def _init_(self):
        distanciaPadraoZeroTip = 0
        distanciaAnteriorZeroTip = 0
        distanciaZeroTip = 0
        pontoTipX = 0
        pontoTipY = 0
        parte1dedo = 0
        parte2dedo = 0
        parte3dedo = 0
        parte4dedo = 0
        parte5dedo = 0 
        divisaoDedo = 0

class Mao:
    def _init_(self):
        pontoZeroX = 0
        pontoZeroY = 0

        polegar = Dedo(0, 0, 0, 0, 0)
        indicador = Dedo(0, 0, 0, 0, 0)
        doMeio = Dedo(0, 0, 0, 0, 0)
        anelar = Dedo(0, 0, 0, 0, 0)
        mindinho = Dedo(0, 0, 0, 0, 0)


#Funcao para calcular a distancia entre dois pontos de uma imagem 2d
def calcularDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia


#Funcao para descobrirmos a coordenada x de um ponto do dedo que especificarmos
def xCoordenada(landmark):
    #return hand_landmarks.landmark[mpHands.HandLandmark(landmark).value].x * image_width
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split('\n')[0].split(" ")[1])


#Funcao para descobrirmos a coordenada y de um ponto do dedo que especificarmos
def yCoordenada(landmark):
    #return hand_landmarks.landmark[mpHands.HandLandmark(landmark).value].y * image_height
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split('\n')[1].split(" ")[1])


#Funcao para o Open CV capturar o video pela camera conectada no USB
cap = cv2.VideoCapture(1)
cap.set(3, 720)  # Define a largura do frame

cap.set(4, 480)  # Define a altura do frame

#Inicia a mao inteira, classe que tem o ponto zero da mao e os dedos
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

            image_height, image_width, _ = maoImagem.shape

            #Nao sei qual jeito de descobrir a coordenada de cada ponto da mao ta certo, entao ta salvo dos dois jeitos

            #Esse jeito de descobrir a coordenada x e y de cada ponto da mao converte para os centimetros do tamanho da foto 
            mao.pontoZeroX = hand_landmarks.landmark[mpHands.HandLandmark(0).value].x *frame_width
            mao.pontoZeroY = hand_landmarks.landmark[mpHands.HandLandmark(0).value].y *frame_heigth

            #Esse jeito de descobrir a coordenada x e y de cada ponto da mao só retorna a coordenada x ou y mesmo
            mao.polegar.pontoTipX = xCoordenada(20)
            mao.polegar.pontoTipy = yCoordenada(20)

            #Armazena a distancia padrao da ponta de cada dedo até o ponto zero da mão 
            mao.polegar.distanciaPadraoZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.polegar.pontoTipX, mao.polegar.pontoTipY)

            mao.polegar.distanciaZeroTip = mao.polegar.distanciaPadraoZeroTip
            mao.polegar.distanciaAnteriorZeroTip = mao.polegar.distanciaPadraoZeroTip

            #Descobre os pontos diferentes da mao (a distancia) em que a ponta do dedo poderia estar em relação ao ponto zero da mao
            mao.polegar.divisaoDedo = mao.polegar.distanciaPadraoZeroTip/5
            mao.polegar.distancia1 = mao.polegar.distanciaPadraoZeroTip
            mao.polegar.distancia2 = mao.polegar.distanciaPadraoZeroTip - mao.polegar.divisaoDedo
            mao.polegar.distancia3 = mao.polegar.distanciaPadraoZeroTip - (mao.polegar.divisaoDedo *2)
            mao.polegar.distancia4 = mao.polegar.distanciaPadraoZeroTip - (mao.polegar.divisaoDedo *3)
            mao.polegar.distancia5 = mao.polegar.distanciaPadraoZeroTip - (mao.polegar.divisaoDedo *4)

            while True:
                hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
                image = cap.read()
                results = hands.process(image)

                mao.pontoZeroX = hand_landmarks.landmark[mpHands.HandLandmark(0).value].x *image_width
                mao.pontoZeroY = hand_landmarks.landmark[mpHands.HandLandmark(0).value].y *image_height

                mao.polegar.pontoTipX = xCoordenada(20)
                mao.polegar.pontoTipy = yCoordenada(20)

                mao.polegar.distanciaZeroTip = calcularDistancia(mao.pontoZeroX, mao.pontoZeroY, mao.polegar.pontoTipX, mao.polegar.pontoTipY)

                #Se identificar que a distancia padrao esta maior que a calculada, quer dizer que a pessoa baixou o dedo
                if (mao.polegar.distanciaAnteriorZeroTip > mao.polegar.distanciaZeroTip):
                    if (mao.polegar.distanciaZeroTip == mao.polegar.distancia2):
                        if (mao.polegar.distanciaAnteriorZeroTip == mao.polegar.distancia1):
                            #baixar 36 graus 1 vez
                    elif (mao.polegar.distanciaZeroTip == mao.polegar.distancia3):
                        if (mao.polegar.distanciaAnteriorZeroTip == mao.polegar.distancia1):
                            #baixar 36 graus 2 vezes
                        elif(mao.polegar.distanciaAnteriorZeroTip == mao.polegar.distancia2):
                            #baixar 36 graus 1 vez
                elif (mao.polegar.distanciaAnteriorZeroTip < mao.polegar.distanciaZeroTip):
                    if (mao.polegar.distanciaZeroTip == mao.polegar.distancia1):
                        if (mao.polegar.distanciaAnteriorZeroTip == mao.polegar.distancia2):
                            #subir 36 graus 1 vez
                        elif (mao.polegar.distanciaAnterior.ZeroTip == mao.polegar.distancia3):
                            #subir 36 graus 2 vezes
                    elif (mao.polegar.distanciaZeroTip == mao.polegar.distancia2):
                        if (mao.polegar.distanciaAnteriorZeroTip == mao.polegar.distancia3):
                            #subir 36 graus 1 vez
                        elif (mao.polegar.distanciaAnteriorZeroTip == mao.polegar.distancia4):
                            #subir 36 graus 2 vezes
                
                distanciaAnteriorZeroPolegar = distanciaZeroPolegar

                k = cv2.waitKey(10)
                if k == ord('q') or k == ord('Q') or k == 27:
                    exit(1)
                elif (k == ord('t')):
                    break
            

cap.release()