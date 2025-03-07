
import cv2 as openCv
import mediapipe
import serial
import time
from classes_mao.Mao import Mao

class Visao:
    def __init__(self):
        # Configuracao da porta serial, que é por onde o arduino vai pegar o arquivo
        self.porta_serial = "/dev/ttyACM0"
        self.baud_rate = 9600

    # Função da visão computacional para fazer com que a mão te imite
    def visaoImitar(self):
        arduino = serial.Serial(self.porta_serial, self.baud_rate)
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
                        mao = Mao(pontos)
                        estadosDedos = mao.analisarDedosMao()

                        mensagem = f"${''.join(map(str, estadosDedos))}"
                        #print(f"Enviando para Arduino: {mensagem}")

                        # Enviando para o Arduino via Serial
                        arduino.write(mensagem.encode())
            openCv.imshow('Imagem', imagem)
            key = openCv.waitKey(1) & 0xFF

            if key == ord('e') or key == ord('E') :
                estadosDedos = [4, 4, 4, 4, 4]
                mensagem = f"${''.join(map(str, estadosDedos))}"

                # Enviando para o Arduino via Serial
                arduino.write(mensagem.encode())
                break
        camera.release()
        openCv.destroyAllWindows()
        messagebox.showinfo("Finalizado", "Movimentos imitados com sucesso!")

    # Função da visão computacional para poder jogar pedra, papel ou tesoura
    def visaoJogar(self):
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
                        mao = Mao(pontos)
                        estadosDedos = mao.analisarDedosMao()
            openCv.imshow('Imagem', imagem)
            key = openCv.waitKey(1) & 0xFF

            if key == ord('j') or key == ord('J') :
                break
        openCv.destroyAllWindows()
        return estadosDedos
    