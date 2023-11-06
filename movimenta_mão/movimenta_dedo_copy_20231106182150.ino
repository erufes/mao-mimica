#include <Servo.h> //INCLUSÃO DA BIBLIOTECA NECESSÁRIA
 
const int pinopolegar = 7; //PINO DIGITAL UTILIZADO PELO SERVO  
const int pinoindicador = 6;
const int pinoanelar = 5;
const int pinomindinho = 4;

Servo polegar;
Servo indicador;
Servo anelar;
Servo mindinho;
 
void setup (){

  polegar.attach(pinopolegar); //ASSOCIAÇÃO DO PINO DIGITAL AO OBJETO DO TIPO SERVO
  indicador.attach(pinoindicador);
  anelar.attach(pinoanelar);
  mindinho.attach(pinomindinho);

}
// void fecha_dedo(){
//   while(1){
//     s.write(0);
//     delay(500);
//     if(s.read() == 0){
//       break;
//     }
//   }
// }
// void abre_dedo(){
//   while(1){
//     s.write(180);
//     delay(500);
//     if(s.read() == 180){
//       break;
//     }
//   }
// }

void loop(){
 
  polegar.write(0);
  delay(1000);
  polegar.write(90);
  delay(1000);
  polegar.write(180);
  delay(1000);
  polegar.write(90);
  delay(1000);

  indicador.write(0);
  delay(1000);
  indicador.write(90);
  delay(1000);
  indicador.write(180);
  delay(1000);
  indicador.write(90);
  delay(1000);

  anelar.write(0);
  delay(1000);
  anelar.write(90);
  delay(1000);
  anelar.write(180);
  delay(1000);
  anelar.write(90);
  delay(1000);

  mindinho.write(0);
  delay(1000);
  mindinho.write(90);
  delay(1000);
  mindinho.write(180);
  delay(1000);
  mindinho.write(90);
  delay(1000);

  
}