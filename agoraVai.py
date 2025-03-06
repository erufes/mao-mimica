import tkinter as tk
import cv2 as openCv
import time
import serial
import mediapipe
from classes_mao.Mao import Mao
from classes_mao.Dedo import Dedo
from tkinter import messagebox

# Configuração da porta serial para o Arduino
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Ajuste conforme necessário
    time.sleep(2)  # Aguarda estabilização
except:
    arduino = None
    print("⚠️ Erro ao conectar ao Arduino. Verifique a porta serial.")

# Variáveis globais de pontuação
placar_usuario = 0
placar_maquina = 0

def iniciar_camera(label_resultado, btn_continuar):
    """Abre a câmera e inicia a detecção da mão (simulação de resultado)"""
    global placar_usuario, placar_maquina

    cap = openCv.VideoCapture(0)  # Abre a câmera (0 = webcam padrão)
    
    if not cap.isOpened():
        messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
        return

    time.sleep(2)
    vencedor = "Usuário" if placar_usuario <= placar_maquina else "Máquina"
    
    # Atualiza a pontuação
    if vencedor == "Usuário":
        placar_usuario += 1
    else:
        placar_maquina += 1

    cap.release()
    openCv.destroyAllWindows()

    label_resultado.config(text=f"Rodada concluída!\n{vencedor} marcou 1 ponto\nUsuário: {placar_usuario} | Máquina: {placar_maquina}")
    btn_continuar.pack(pady=10)

    if placar_usuario == 2 or placar_maquina == 2:
        messagebox.showinfo("Fim de Jogo", f"{vencedor} venceu o melhor de 3!")
        mostrar_menu()  # Volta ao menu principal

def contagem_regressiva(label, segundos, label_resultado, btn_continuar, btn_iniciar):
    """Faz a contagem regressiva antes de abrir a câmera"""
    btn_iniciar.pack_forget()  # Esconde o botão iniciar
    
    if segundos > 0:
        label.config(text=f"Iniciando em {segundos}...")
        janela.after(1000, contagem_regressiva, label, segundos - 1, label_resultado, btn_continuar, btn_iniciar)
    else:
        label.config(text="Captura iniciada!")
        iniciar_camera(label_resultado, btn_continuar)

def iniciar_jogo():
    """Altera a interface para o modo de jogo"""
    global placar_usuario, placar_maquina
    placar_usuario = 0
    placar_maquina = 0

    for widget in janela.winfo_children():
        widget.destroy()

    frame_inicio = tk.Frame(janela, bg="#FFC0CB")
    frame_inicio.place(relx=0.5, rely=0.5, anchor="center")

    label_instrucao = tk.Label(frame_inicio, text="Pronto para iniciar?", font=("Arial", 36), bg="#FFC0CB")
    label_instrucao.pack(pady=5)

    label_resultado = tk.Label(frame_inicio, text="", font=("Arial", 22), bg="#FFC0CB")
    label_resultado.pack(pady=5)

    btn_continuar = tk.Button(frame_inicio, text="Continuar", font=("Arial", 22), bg="white", fg="black",
                              command=lambda: contagem_regressiva(label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))

    btn_iniciar = tk.Button(frame_inicio, text="Iniciar", font=("Arial", 25), bg="white", fg="black",
                            command=lambda: contagem_regressiva(label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))
    btn_iniciar.pack(pady=20)

def replicar_movimentos():
    """Abre a câmera, detecta a mão e envia comandos ao Arduino"""
    if arduino is None:
        messagebox.showerror("Erro", "Conexão com Arduino não estabelecida.")
        return

    camera = openCv.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)

    hands = mediapipe.solutions.hands
    Hands = hands.Hands(max_num_hands=1)
    mediapipeDraw = mediapipe.solutions.drawing_utils

    messagebox.showinfo("Instrução", "Movimente sua mão para enviar comandos ao Arduino.\nPressione 'F' para encerrar.")

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
                    openCv.circle(imagem, (coordenadaX, coordenadaY), 4, (255, 0, 0), -1)
                    pontos.append((coordenadaX, coordenadaY))

                if pontos:
                    mao = Mao(pontos)
                    estadosDedos = mao.analisarDedosMao()

                    mensagem = f"${''.join(map(str, estadosDedos))}"
                    print(f"Enviando para Arduino: {mensagem}")

                    # Enviando para o Arduino via Serial
                    arduino.write(mensagem.encode())

        openCv.imshow('Imagem', imagem)
        key = openCv.waitKey(1) & 0xFF

        if key == ord('f') or key == ord('F'):
            estadosDedos = [4, 4, 4, 4, 4]
            mensagem = f"${''.join(map(str, estadosDedos))}"
            print("Fechando o programa.")

            arduino.write(mensagem.encode())
            break

    camera.release()
    openCv.destroyAllWindows()
    messagebox.showinfo("Finalizado", "Movimentos replicados com sucesso!")

def mostrar_menu():
    """Exibe o menu inicial"""
    for widget in janela.winfo_children():
        widget.destroy()

    frame_menu = tk.Frame(janela, bg="#FFC0CB")
    frame_menu.place(relx=0.5, rely=0.45, anchor="center")

    label_titulo = tk.Label(frame_menu, text="Menu", font=("Arial", 40), bg="#FFC0CB")
    label_titulo.pack(pady=20)

    btn_replicar = tk.Button(frame_menu, text="Replicar Movimentos", 
                             command=replicar_movimentos, 
                             width=25, font=("Arial", 22), bg="white", fg="black")
    btn_replicar.pack(pady=15)

    btn_jogar = tk.Button(frame_menu, text="Jogar", command=iniciar_jogo, 
                          width=25, font=("Arial", 22), bg="white", fg="black")
    btn_jogar.pack(pady=15)

    btn_sair = tk.Button(frame_menu, text="Sair", command=janela.quit, 
                         width=25, font=("Arial", 22), bg="red", fg="white")
    btn_sair.pack(pady=15)

# Criando a janela principal
janela = tk.Tk()
janela.title("Jogo de Detecção de Mãos")
janela.attributes('-fullscreen', True)
janela.configure(bg="#FFC0CB")

mostrar_menu()

janela.mainloop()