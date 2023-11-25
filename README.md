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

<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>

## 📝 Descrição do Projeto
O projeto consiste em uma mão impressa em 3D que imita os movimentos da mão do usuário apresentada na webCam.

## 👾 Funcionamento
### Software
Refere-se a parte de leitura da movimentação da mão do usuário. Essa interpretação dos movimentos foi realizada na linguagem de programação Python, utilizando a biblioteca MediaPipe e OpenCV. Cada dedo da mão impressa tem 
marcações de cada uma de suas articulações, sendo que usaremos da marcação na ponta do dedo e onde liga o dedo a mão.
### Hardware
Consiste na movimentação da mão impressa em 3D. Junto de um arduíno e servo-motores, partindo da interpretação dos movimentos da mão do usuário, é possível saber qual ângulo precisamos girar em cada dedo da mão impressa.
A movimentação da mão impressa foi realizada em C++.

## 📚 Libs Usadas
### Open CV
É uma biblioteca de programação, de código aberto, e inicialmente desenvolvida pela Intel com o objetivo de tornar a visão computacional mais acessível a desenvolvedores e hobistas. Atualmente possui mais de 500 
funções, pode ser utilizada em diversas linguagens de programação (C++, Python, Ruby, Java…) e é usada para diversos tipos de análise em imagens e vídeos, como  detecção, tracking e reconhecimento facial, edição de fotos e vídeos, detecção e análise de textos, etc. 
### MediaPipe
É uma plataforma de código aberto mantida pelo Google, que oferece um conjunto abrangente de ferramentas, APIs e modelos pré-treinados que facilitam a construção de aplicações para tarefas como estimativa de pose, detecção de objetos, reconhecimento facial, entre outras.

## 🏗️ Estrutura
### Arduino <img loading="lazy" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg" width="30" height="30"/>



## 🔨 Implementações futuras
Se tratando de um projeto em desenvolvimento, falta implementar:
- [ ] Identificação e interpretação dos movimentos da mão do usuário;
- [ ] Transferencia da interpretação dos movimentos para o arduino;
- [ ] Interpretação da informação coletada e execução do ângulo referente ao que foi solicitado;
- [ ] Desafio, que consiste em fazer um modo de jogo que seria possível jogar Pedra, papel, tesoura, lagarto e Spock contra a mão impressa em 3D. 
 
## 📌 Pré-requisitos
```pip install opencv-python```

```pip install mediapipe```

## 👩‍💻 Desenvolvedores
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136736744?v=4" width=115><br><sub>Diana Mello Rosi</sub>](https://github.com/dianamross) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/136653897?v=4" width=115><br><sub>Elisa Muller Sarmento</sub>](https://github.com/BeWSM) |
| :---: | :---: |
