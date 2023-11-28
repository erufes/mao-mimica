import cv2
import math
import mediapipe as mp

mpDrawing = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)


#Funcao para calcular a distancia entre dois pontos de uma imagem 2d
def calcularDistancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia


#Funcao para descobrirmos a coordenada x de um ponto do dedo que especificarmos
def xCoordenada(landmark):
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split('\n')[0].split(" ")[1])


#Funcao para descobrirmos a coordenada y de um ponto do dedo que especificarmos
def yCoordenada(landmark):
    return float(str(results.multi_hand_landmarks[-1].landmark[int(landmark)]).split('\n')[1].split(" ")[1])


#Funcao para o Open CV capturar o video pela camera conectada no USB
cap = cv2.VideoCapture(1)
cap.set(3, 720)  # Define a largura do frame
cap.set(4, 480)  # Define a altura do frame

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
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
    cv2.imshow("MediaPipe Hands", image)

    #Descobrimos o x e o y do ponto zero da mao 
    pontoZeroX = xCoordenada(0)
    pontoZeroY = yCoordenada(0)

    pontoTipPolegarX = xCoordenada(20)
    pontoTipPolegarY = yCoordenada(20)

    distanciaPadraoZeroPolegar = calcularDistancia(pontoZeroX, pontoZeroY, pontoTipPolegarX, pontoTipPolegarY)
    #ai pensei no programa meio que prever quanto de distancia ficaria do ponto zero da mao ate a ponta do mindinho
    #ai se a distancia calculada for igual a distancia premeditada do dedo no meio termo (nem totalmente aberto nem totalemnte fechado), ele manda mexer o angulo
    # equivalente a quantidade da distancia calcular.
    # se calculou que ele mexeu 2 medidas de distancia, ele mexe o angulo especificado 2 vezes (para cima ou para baixo, isso teria q ser fazendo a diferenca entre o ponto zero
    # e o ponto onde a ponta do dedo esta e pra onde ele deve ir) 

    distanciaAnteriorZeroPolegar = distanciaPadraoZeroPolegar

    while EhMesmaMao:
        pontoZeroX = xCoordenada(0)
        pontoZeroY = yCoordenada(0)

        pontoTipPolegarX = xCoordenada(4)
        pontoTipPolegarY = yCoordenada(4)

        distanciaZeroPolegar = calcularDistancia(pontoZeroX, pontoZeroY, pontoTipPolegarX, pontoTipPolegarY)

        #Se identificar que a distancia padrao esta maior que a calculada, quer dizer que a pessoa baixou o dedo
        if (distanciaAnteriorZeroPolegar > distanciaZeroPolegar):
            if (distanciaZeroPolegar == distanciaTipPolegar1):
                #baixar 36 graus
            elif (distanciaZeroPolegar == distanciaTipPolegar2):
                #baixar 36 graus
                #baixar 36 graus
        elif (distanciaAnterior < distanciaZeroPolegar):
            if (distanciaZeroPolegar == distanciaTipPolegar1):
                #subir 36 graus
        
        distanciaAnteriorZeroPolegar = distanciaZeroPolegar

    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()