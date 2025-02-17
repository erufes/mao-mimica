# LISTA DO QUE PRECISA FAZER (mais ou menos tudo o que precisa)
#(X) conseguir identificar se todos os dedos estão fechados completamente
#(X) conseguir mandar para o codigo do arduino (talvez em um arquivo json)
#( ) ver se o arduino ta recebendo certo
#(X) conseguir saber a movimentacao exata do dedo (se ta completamente aberto, se ta quase aberto, se ta na metade do movimento, se ta quase fechado, se ta completamente fechado)
#(X) conseguir o ultimo topico para todos os dedos
#( ) classe mao
#( ) classe dedo 
#( ) fazer funcionar com as classes
#( ) modo de jogo pedra papel e tesoura (ai precisa de outra listinha)

import cv2 as openCv
import mediapipe
import json

movimentosMao = [0, 0, 0, 0, 0]
camera = openCv.VideoCapture(0)

camera.set(3,640)
camera.set(4,480)

hands = mediapipe.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mediapipeDraw = mediapipe.solutions.drawing_utils

while True:
    success, imagem = camera.read()
    frameRGB = openCv.cvtColor(imagem, openCv.COLOR_BGR2RGB)
    resultados = Hands.process(frameRGB)
    pontosMao = resultados.multi_hand_landmarks
    altura, largura, _ = imagem.shape
    pontos = []
    if pontosMao:
        for points in pontosMao:
            mediapipeDraw.draw_landmarks(imagem, points, hands.HAND_CONNECTIONS)
            for id, coordenada in enumerate(points.landmark):
                coordenadaX, coordenadaY = int(coordenada.x * largura), int(coordenada.y * altura)
                openCv.circle(imagem, (coordenadaX, coordenadaY), 4, (255,0,0), -1)
                pontos.append((coordenadaX, coordenadaY))

            if pontos:
                distanciaPolegar = abs(pontos[17][0] - pontos[4][0])
                distanciaIndicador = pontos[5][1] - pontos[8][1]
                distanciaMedio = pontos[9][1] - pontos[12][1]
                distanciaAnelar = pontos[13][1] - pontos[16][1]
                distanciaMinimo = pontos[17][1] - pontos[20][1]

                print("..........................................")

                if distanciaPolegar <70:
                    print("POLEGAR TOTALMENTE FECHADO")
                    polegar = 0
                elif distanciaPolegar <100:
                    print("POLEGAR QUASE TOTALMENTE FECHADO")
                    polegar = 1
                elif distanciaPolegar <140:
                    print("POLEGAR MEIO TERMO")
                    polegar = 2
                elif distanciaPolegar <180:
                    print("POLEGAR QUASE TOTALMENTE ABERTO")
                    polegar = 3
                else:
                    print("POLEGAR TOTALMENTE ABERTO")
                    polegar = 4
                movimentosMao[0] = polegar

                if distanciaIndicador <10:
                    print("INDICADOR TOTALMENTE FECHADO")
                    indicador = 0
                elif distanciaIndicador <50:
                    print("INDICADOR QUASE TOTALMENTE FECHADO")
                    indicador = 1
                elif distanciaIndicador <80:
                    print("INDICADOR MEIO TERMO")
                    indicador = 2
                elif distanciaIndicador <100:
                    print("INDICADOR QUASE TOTALMENTE ABERTO")
                    indicador = 3
                else:
                    print("INDICADOR TOTALMENTE ABERTO")
                    indicador = 4
                movimentosMao[1] = indicador

                if distanciaMedio <-10:
                    print("MEDIO TOTALMENTE FECHADO")
                    medio = 0
                elif distanciaMedio <10:
                    print("MEIO QUASE TOTALMENTE FECHADO")
                    medio = 1
                elif distanciaMedio <60:
                    print("MEIO MEIO TERMO")
                    medio = 2
                elif distanciaMedio <110:
                    print("MEDIO QUASE TOTALMENTE ABERTO")
                    medio = 3
                else:
                    print("MEDIO TOTALMENTE ABERTO")
                    medio = 4
                movimentosMao[2] = medio

                if distanciaAnelar <-20:
                    print("ANELAR TOTALMENTE FECHADO")
                    anelar = 0
                elif distanciaAnelar <10:
                    print("ANELAR QUASE TOTALMENTE FECHADO")
                    anelar = 1
                elif distanciaAnelar <60:
                    print("ANELAR MEIO TERMO")
                    anelar = 2
                elif distanciaAnelar <110:
                    print("ANELAR QUASE TOTALMENTE ABERTO")
                    anelar = 3
                else:
                    print("ANELAR TOTALMENTE ABERTO")
                    anelar = 4
                movimentosMao[3] = anelar

                if distanciaMinimo <0:
                    print("MINIMO TOTALMENTE FECHADO")
                    minimo = 0
                elif distanciaMinimo <30:
                    print("MINIMO QUASE TOTALMENTE FECHADO")
                    minimo = 1
                elif distanciaMinimo <50:
                    print("MINIMO MEIO TERMO")
                    minimo = 2
                elif distanciaMinimo<70:
                    print("MINIMO QUASE TOTALMENTE ABERTO")
                    minimo = 3
                else:
                    print("MINIMO TOTALMENTE ABERTO")
                    minimo = 4
                movimentosMao[4] = minimo

                with open('movimentos.json', 'w') as file:
                    json.dump({"movimentos": movimentosMao}, file)
            

    openCv.imshow('Imagem', imagem)
    openCv.waitKey(1)