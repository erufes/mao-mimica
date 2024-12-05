//Codigo que recebe quais dedos da mao mimica devem fechar ou abrir conforme o codigo de visao computacional observou

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


void loop() {
  data();
  
  if (valoresRecebidos[0] == 1) { servoPolegar.write(180); }        //se a funcao data retornou 1 na posicao da string que representa o polegar, quer dizer que o dedo levanta (ou seja, manda o servo motor rodar 180 graus no sentido antihorario)
  else { servoPolegar.write(0); }                                   //se retornou 0, quer dizer que o dedo abaixou (ou seja, manda o servo motor rodar 180 graus no sentido horario)

  if (valoresRecebidos[1] == 1) { servoIndicador.write(180); } 
  else { servoIndicador.write(0); }

  if (valoresRecebidos[2] == 1) { servoMeio.write(180); } 
  else { servoMeio.write(0); }

  if (valoresRecebidos[3] == 1) { servoAnelar.write(180); } 
  else { servoAnelar.write(0); }

  if (valoresRecebidos[4] == 1) { servoMindinho.write(180); } 
  else { servoMindinho.write(0); }


}










