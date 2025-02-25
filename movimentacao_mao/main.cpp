//Codigo que recebe quais dedos da mao mimica devem fechar ou abrir conforme o codigo de visao computacional observou

#include <Arduino.h>
#include <Servo.h>

Servo servoPolegar;
Servo servoIndicador;
Servo servoMeio;
Servo servoAnelar;
Servo servoMindinho;

#define qtdValoresRecebidos 5
#define digitosValorRecebido 1

int valoresRecebidos[qtdValoresRecebidos];
int tamanhoString = qtdValoresRecebidos * digitosValorRecebido +1;    //$00000
int contador = 0;
bool contadorStart = false;
String stringRecebida;


void setup() {
  Serial.begin(9600);
  servoPolegar.attach(7);
  servoIndicador.attach(9);
  servoMeio.attach(11);
  servoAnelar.attach(8);
  servoMindinho.attach(10);
}


void data() {
  while(Serial.available()) {
    char c = Serial.read();

    if (c == '$') {
      contadorStart = true;
    }

    if (contadorStart) {
      if (contador < tamanhoString) {
        stringRecebida = String(stringRecebida+c);
        contador++;
      }

      if (contador >= tamanhoString) {
        for(int i=0; i<qtdValoresRecebidos; i++) {
          int num = (i*digitosValorRecebido)+1;
          valoresRecebidos[i] = stringRecebida.substring(num, num + digitosValorRecebido).toInt();
        }

        stringRecebida = "";
        contador = 0;
        contadorStart = false;
      }
    }
  }
}

int associaAngulo (int detectado) {
  int angulo;

  if(detectado == 0) angulo = 180;
  else if(detectado == 1) angulo = 135;
  else if (detectado == 2) angulo = 90;
  else if (detectado == 3) angulo = 45;
  else angulo = 0;

  return angulo;
}


void loop() {
  data();
  int angulo;
  
  angulo = associaAngulo(valoresRecebidos[0]);
  servoPolegar.write(angulo);

  angulo = associaAngulo(valoresRecebidos[1]);
  servoIndicador.write(angulo);

  angulo = associaAngulo(valoresRecebidos[2]);
  servoMeio.write(angulo);

  angulo = associaAngulo(valoresRecebidos[3]);
  servoAnelar.write(angulo);

  angulo = associaAngulo(valoresRecebidos[4]);
  servoMindinho.write(angulo);
}