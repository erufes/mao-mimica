
import cv2 as openCv
import mediapipe
import json
import serial
import time
import classes.Mao as Mao

# Configuracao da porta serial, que é por onde o arduino vai pegar o arquivo
porta_serial = "/dev/ttyACM0"

baud_rate = 9600
arduino = serial.Serial(porta_serial, baud_rate)
time.sleep(2) 

camera = openCv.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)

hands = mediapipe.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mediapipeDraw = mediapipe.solutions.drawing_utils

class MaoMimica:
    

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
                mao = Mao()
                estadosDedos = mao.analisarDedosMao(mao, pontos)

                mensagem = f"${''.join(map(str, estadosDedos))}"
                print(f"Enviando para Arduino: {mensagem}")

                # Enviando para o Arduino via Serial
                arduino.write(mensagem.encode())

                with open('estados.json', 'w') as file:
                    json.dump({"estados": estadosDedos}, file)

    openCv.imshow('Imagem', imagem)
    openCv.waitKey(1)
