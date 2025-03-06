
import cv2 as openCv
import mediapipe
import json
import serial
import time

import classes_mao.Mao as Mao
import classes_mao.Dedo as Dedo

import classes_menu.Menu as Menu
import classes_menu.MaoMimica as MaoMimica
import classes_menu.Jogo as Jogo

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
                menu = Menu(pontos, imagem, openCv)

    openCv.imshow('Imagem', imagem)
    