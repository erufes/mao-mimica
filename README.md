# braco-mimico
## Descrição:
O projeto tem como objetivo a construção de uma mão mímica capaz de copiar gestos e sinais apresentados em frente à uma câmera.

## Funcionalidades:
O programa ao ser executado recebe informações via webcam de uma mão, que sera trackeada e utilizada como "espelho" para a mão mímica impressa em 3D.

## Desafio a ser implementado:
Brincar com a mão mímica de Pedra-papel-tesoura: em que o usuário (a mão apresentada na webcam) joga contra a mão mímica. Ao longo da partida, a máquina iria calculando as probabilidades de sinais que o usuário vai usar, prevendo o próximo sinal, com base nos sinais mais usados anteriormente. Dessa forma, além de utilizar da visão computacional, iria implementar também machine learning.

![Exemplo de mão trackeada](https://programacionpython80889555.files.wordpress.com/2021/06/annotated_imageh0.png)

## Funcionamento:
Para o programa funcionar adequadamente é preciso instalar as bibliotecas OpenCv:
- pip3 install opencv-python