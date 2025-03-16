<h1 align= "center"> ✋ Mão Mímica 🤖 </h1>

<div align="center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GitHub latest commit](https://badgen.net/github/last-commit/erufes/mao-mimica)](https://GitHub.com/erufes/mao-mimica/commit/)
[![GitHub commits](https://badgen.net/github/commits/erufes/mao-mimica)](https://GitHub.com/erufes/mao-mimica/commit/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/erufes/mao-mimica)](https://GitHub.com/erufes/mao-mimica/pull/)
[![GitHub branches](https://badgen.net/github/branches/erufes/mao-mimica)](https://github.com/erufes/mao-mimica/)

<img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40"/> <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" width="40" height="40"/>

</div>

## 📝 Descrição do Projeto
O projeto consiste em uma mão robótica impressa em 3D e uma interface de menu que permite ao usuário interagir com a mão. O menu oferece duas opções principais: a primeira é a reprodução dos movimentos da mão do usuário, e a segunda é um jogo de Pedra, Papel e Tesoura contra a mão robótica. Utilizando uma webcam, o sistema é capaz de identificar, por meio de técnicas de visão computacional, quais dedos da mão do usuário estão abertos ou fechados, permitindo a captura e interpretação dos movimentos. Para a movimentação dos dedos da mão robótica, são empregados motores e plataformas programáveis. Um vídeo demonstrativo do funcionamento da mão, desenvolvido para a disciplina de PIC 1, está disponível neste [link](https://youtube.com/shorts/ycraxiblsJk?si=14KT6FwUJX3uGOeN).

<img width="125" heigth="125" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/maoFrente.png"> <img width="100" heigth="100" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/maoAntebraco.png"> <img width="125" heigth="125" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/maoCosta.png">

### Imitar movimentos ✋
Por meio da visão computacional, o sistema é capaz de reconhecer os movimentos realizados pelo usuário em frente à webcam. Para isso, foram definidos cinco estados possíveis para cada dedo: totalmente fechado, quase totalmente fechado, meio termo, quase totalmente aberto e totalmente aberto. Cada transição entre esses estados é controlada por quatro ângulos pré-determinados, que orientam o movimento dos servomotores responsáveis pela movimentação dos dedos. O programa utiliza uma lista de cinco posições, em que cada posição corresponde a um dedo da mão. Com base nessa lista, o sistema identifica o estado atual de cada dedo e envia essas informações para o Arduino. No Arduino, um código recebe a lista de estados e calcula quantos ângulos cada servomotor precisa girar para replicar os movimentos da mão do usuário. Dessa forma, a mão robótica consegue imitar, de maneira precisa e sincronizada, os gestos realizados pelo usuário.
 
### Jogar Pedra, Papel e Tesoura 🎮
O modo de jogo segue quase a mesma lógica de imitar os movimentos da mão do usuário, sendo que são pré-determinados três movimentos possíveis do usuário: pedra (que seria a lista 0, 0, 0, 0, 0), papel (4, 4, 4, 4, 4) e tesoura (0, 4, 4, 0, 0). Assim, o programa identifica qual foi a jogada do usuário, sendo que foi implementada uma margem de tolerância (ou seja, caso a pessoa jogue pedra mas o programa identifique a lista 0, 1, 0, 0, 0 ele ainda vai reconhecer como pedra graças a tolerância). A mão robótica tem esses mesmas três listas de movimento como opção, sendo que ela deve escolher um aleatoriamente e mandar pro arduino para poder realizar a sua jogada. Dessa forma, o programa armazena qual foi a jogada do usuário e a da mão robótica, pontuando o vencedor da rodada e eventualmente, o vencedor da partida.

## 👾 Funcionamento
### Software
Refere-se à parte de leitura da movimentação da mão do usuário. Essa interpretação dos movimentos será realizada na linguagem de programação Python, utilizando as bibliotecas MediaPipe e OpenCV. Cada dedo da mão impressa tem marcações de cada uma de suas articulações e, utilizando das bibliotecas citadas, podemos saber qual dedo está aberto ou fechado.

<img width="500" heigth="500" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/hand_landmarks.png">

### Hardware
Consiste na movimentação da mão impressa em 3D. Junto de um arduino uno e servo motores, partindo da interpretação dos movimentos da mão do usuário, é possível saber qual ângulo precisamos girar em cada dedo da mão impressa. A movimentação da mão impressa é realizada em C++. Na imagem abaixo mostra como os servo motores ficam na estrutura interna do antebraço.

<img width="150" heigth="150" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/antebraco.png">

## 📚 Libs Usadas
### Open CV <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" width="25" height="25"/>
É uma biblioteca de programação, de código aberto, e inicialmente desenvolvida pela Intel com o objetivo de tornar a visão computacional mais acessível a desenvolvedores e hobistas. Atualmente possui mais de 500 funções, pode ser utilizada em diversas linguagens de programação (C++, Python, Ruby, Java…) e é usada para diversos tipos de análise em imagens e vídeos, como detecção, tracking e reconhecimento facial, edição de fotos e vídeos, detecção e análise de textos, etc. Usaremos para a manipulação da webcam e para a identificação da mão.
### MediaPipe <img width="25" heigth="25" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/mediaPipeLogo.png">
É uma plataforma de código aberto mantida pelo Google, que oferece um conjunto abrangente de ferramentas, APIs e modelos pré-treinados que facilitam a construção de aplicações para tarefas como estimativa de pose, detecção de objetos, reconhecimento facial, entre outras. Usaremos para identificar cada articulação da mão, sendo possível saber qual dedo está levantado ou abaixado.

## 🏗️ Estrutura
### Arduino <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg" width="25" height="25"/>
É uma plataforma programável de prototipagem eletrônica de placa única e hardware livre, que permite aos usuários criar objetos eletrônicos interativos e independentes, usando o microcontrolador Atmel AVR ou ARM com suporte de entrada/saída embutido, uma linguagem de programação padrão, essencialmente C/C++.

<img width="200" heigth="200" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/arduinoUno.png">

### Modelo da mão 3D InMoov
O modelo 3D da mão pegamos do InMoov, projeto pessoal do escultor e designer francês Gael Langevin, iniciado em janeiro de 2012 como a primeira mão protética de código aberto. Esse projeto deu origem a iniciativas como Bionico, E-Nable e muitas outras. O InMoov é o primeiro robô em tamanho real impresso em 3D de código aberto. Reproduzível em qualquer impressora 3D doméstica com uma área de 12x12x12 cm, foi concebido como uma plataforma de desenvolvimento para universidades, laboratórios, entusiastas, mas, acima de tudo, para makers. O modelo está disponível no site InMoov Mão e Antebraço.

### WebCam
Precisaremos da webcam conectada a um computador, ou notebook, para podermos capturar os movimentos da mão do usuário e replicá-los na mão mímica. Usaremos a webcam HD C270 da Logitech.

### Servo Motores
Cada dedo precisa estar conectado por fios (usamos linha de pesca por ser mais resistente) a um servo-motor para ser capaz de replicar os movimentos captados pela câmera. Estão sendo usados 5 servo motores MG996R 180° Tower Pro. Eles só são capazes de girar em 180°, que é o necessário para fazer os movimentos de abrir ou fechar os dedos. Na foto abaixo, é possível observar como os motores estão dentro do antebraço.

<img width="200" heigth="200" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/servoMotor.png">
 
## 📌 Pré-requisitos
```pip install opencv-python```

```pip install mediapipe```

```pip install pyserial```

## ☝️🤓 Instruções
- As bibliotecas descritas no tópico anterior devem ser baixadas pelo terminal. Além disso, Python também deve estar presente na máquina.
- O código 'main.cpp' localizado na pasta 'src/hardware' deve ser mandado para o arduino. Usamos o Arduino IDE para fazer o upload do código no arduino, sendo que precisamos baixar a biblioteca 'Servo.h' dentro do próprio Arduino IDE.
- No código 'Jogo.py' e 'MaoMimica.py' precisa inserir nas linhas 20 e 13 em qual porta serial do computador o arduino está conectado (nós descobrimos a porta serial ao mandar o código 'main.cpp' para o arduino pelo Arduino IDE).
- É preciso uma fonte de 5 a 7,2 volts para energizar o circuito dos servo motores, sendo que o GND conecta no jumper escuro e a fonte conecta no jumper claro.
- Além disso, precisa de uma webcam conectada. Nos códigos 'Jogo.py' e 'MaoMimica.py', nas linhas 78 e 21, é possível configurar a câmera do computador nos parêntes, sendo que 0 é quando deseja usar a primeira opção de captura de vídeo do computador.
- Dessa forma, para o código rodar é preciso enviar o comando abaixo no terminal:

```python3 main.py```

## 👩‍💻 Desenvolvedoras
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136736744?v=4" width=115><br><sub>Diana Mello Rosi</sub>](https://github.com/dianamross) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136653897?v=4" width=115><br><sub>Elisa Muller</sub>](https://github.com/BeWSM) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/149831641?v=4" width=115><br><sub>Rafaela Capovilla</sub>](https://github.com/rafacpovilla) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/149822230?v=4" width=115><br><sub>Rafaela Fernanda</sub>](https://github.com/rafaxxix) |
| :---: | :---: | :---: | :---: |
