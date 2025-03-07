import tkinter as tk
import cv2
import time
from tkinter import messagebox

# Variáveis globais de pontuação
placar_usuario = 0
placar_maquina = 0

def iniciar_camera(label_resultado, btn_continuar):
    """Abre a câmera e inicia a detecção da mão (simulação de resultado)"""
    global placar_usuario, placar_maquina

    cap = cv2.VideoCapture(0)  # Abre a câmera (0 = webcam padrão)
    
    if not cap.isOpened():
        messagebox.showerror("Erro", "Não foi possível acessar a câmera.")
        return

    # Simula um tempo de processamento e decide um vencedor aleatório
    time.sleep(2)
    vencedor = "Usuário" if placar_usuario <= placar_maquina else "Máquina"
    
    # Atualiza a pontuação
    if vencedor == "Usuário":
        placar_usuario += 1
    else:
        placar_maquina += 1

    cap.release()
    cv2.destroyAllWindows()

    # Atualiza o placar na interface
    label_resultado.config(text=f"Rodada concluída!\n{vencedor} marcou 1 ponto\nUsuário: {placar_usuario} | Máquina: {placar_maquina}")
    btn_continuar.pack(pady=10)

    # Verifica se alguém venceu (melhor de 3)
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

    # Remove os botões do menu
    for widget in janela.winfo_children():
        widget.destroy()

    frame_inicio = tk.Frame(janela, bg="#FFC0CB")
    frame_inicio.place(relx=0.5, rely=0.5, anchor="center")

    # Novo layout da tela de jogo
    label_instrucao = tk.Label(frame_inicio, text="Pronto para iniciar?", font=("Arial", 36), bg="#FFC0CB")
    label_instrucao.pack(pady=5)

    label_resultado = tk.Label(frame_inicio, text="", font=("Arial", 22), bg="#FFC0CB")
    label_resultado.pack(pady=5)

    btn_continuar = tk.Button(frame_inicio, text="Continuar", font=("Arial", 22), bg="white", fg="black",
                              command=lambda: contagem_regressiva(label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))

    btn_iniciar = tk.Button(frame_inicio, text="Iniciar", font=("Arial", 25), bg="white", fg="black",
                            command=lambda: contagem_regressiva(label_resultado, 3, label_resultado, btn_continuar, btn_iniciar))
    btn_iniciar.pack(pady=20)


def mostrar_menu():
    for widget in janela.winfo_children():
        widget.destroy()

    # Criando um frame central para agrupar os elementos
    frame_menu = tk.Frame(janela, bg="#FFC0CB")
    frame_menu.place(relx=0.5, rely=0.45, anchor="center")  # Centraliza no meio da tela

    # Título do menu
    label_titulo = tk.Label(frame_menu, text="Menu", font=("Arial", 40), bg="#FFC0CB")
    label_titulo.pack(pady=20)  # Pequeno espaçamento abaixo do título

    # Botão "Replicar Movimentos"
    btn_replicar = tk.Button(frame_menu, text="Replicar Movimentos", 
                            command=lambda: messagebox.showinfo("Replicar Movimentos", "Funcionalidade ainda não implementada."), 
                            width=25, font=("Arial", 22), bg="white", fg="black")
    btn_replicar.pack(pady=15)  # Espaçamento entre os botões

    # Botão "Jogar"
    btn_jogar = tk.Button(frame_menu, text="Jogar", command=iniciar_jogo, 
                        width=25, font=("Arial", 22), bg="white", fg="black")
    btn_jogar.pack(pady=15)

    # Botão "Sair"
    btn_sair = tk.Button(frame_menu, text="Sair", command=janela.quit, 
                        width=25, font=("Arial", 22), bg="red", fg="white")
    btn_sair.pack(pady=15)


# Criando a janela principal
janela = tk.Tk()
janela.title("Jogo de Detecção de Mãos")
janela.attributes('-fullscreen', True)  # Ocupa a tela inteira
janela.configure(bg="#FFC0CB")

# Exibe o menu ao iniciar
mostrar_menu()

# Rodando a interface
janela.mainloop()