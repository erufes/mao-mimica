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
O projeto consiste em uma mão impressa em 3D e um menu por onde o usuário vai fazer a sua interação com a mão. O menu contém duas opções, sendo que a primeira é a reprodução dos movimentos da mão do usuário, e a segunda é jogar Pedra, Papel e Tesoura contra a mão robótica. Por meio de uma webcam, o programa é capaz de identificar quais dedos o usuário tem aberto ou fechado, sendo possível identificar seus movimentos fazendo uso de visão computacional. Além disso, usa-se também plataformas programáveis e motores para possibilitar a movimentação dos dedos da mão.

<img width="125" heigth="125" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/maoFrente.png"> 
<img width="100" heigth="100" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/maoAntebraco.png">
<img width="125" heigth="125" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/maoCosta.png">

### Imitar movimentos ✋

### Jogar Pedra, Papel e Tesoura 🎮

## 👾 Funcionamento
### Software
Refere-se à parte de leitura da movimentação da mão do usuário. Essa interpretação dos movimentos será realizada na linguagem de programação Python, utilizando as bibliotecas MediaPipe e OpenCV. Cada dedo da mão impressa tem marcações de cada uma de suas articulações e, utilizando das bibliotecas citadas, podemos saber qual dedo está aberto ou fechado.

<img width="500" heigth="500" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/hand_landmarks.png">

### Hardware
Consiste na movimentação da mão impressa em 3D. Junto de um arduino uno e servo motores, partindo da interpretação dos movimentos da mão do usuário, é possível saber qual ângulo precisamos girar em cada dedo da mão impressa. A movimentação da mão impressa é realizada em C++.

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
Cada dedo precisa estar conectado por fios (usamos linha de pesca por ser mais resistente) a um servo-motor para ser capaz de replicar os movimentos captados pela câmera. Estão sendo usados 5 servo motores MG996R 180° Tower Pro. Eles só são capazes de girar em 180°, que é o necessário para fazer os movimentos de abrir ou fechar os dedos. Na foto abaixo, é possível observar como os motores estão dentro do antebraço. Abaixo temos a imagem da direita que mostra como os servo motores ficam na estrutura interna do antebraço.

<img width="200" heigth="200" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/servoMotor.png">  <img width="125" heigth="125" src="https://github.com/erufes/mao-mimica/blob/main/forREAD_ME/imagens/antebraco.png">
 
## 📌 Pré-requisitos
```pip install opencv-python```

```pip install mediapipe```

## 👩‍💻 Desenvolvedoras
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136736744?v=4" width=115><br><sub>Diana Mello Rosi</sub>](https://github.com/dianamross) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136653897?v=4" width=115><br><sub>Elisa Muller</sub>](https://github.com/BeWSM) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/149831641?v=4" width=115><br><sub>Rafaela Capovilla</sub>](https://github.com/rafacpovilla) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/149822230?v=4" width=115><br><sub>Rafaela Fernanda</sub>](https://github.com/rafaxxix) |
| :---: | :---: | :---: | :---: |
