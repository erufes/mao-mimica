#include <Servo.h> //INCLUSÃO DA BIBLIOTECA NECESSÁRIA
 
const int pinoServo = 6; //PINO DIGITAL UTILIZADO PELO SERVO  
 
Servo s; //OBJETO DO TIPO SERVO
int pos; //POSIÇÃO DO SERVO
 
void setup (){
  s.attach(pinoServo); //ASSOCIAÇÃO DO PINO DIGITAL AO OBJETO DO TIPO SERVO
}
void fecha_dedo(){
  while(1){
    s.write(0);
    delay(500);
    if(s.read() == 0){
      break;
    }
  }
}
void abre_dedo(){
  while(1){
    s.write(180);
    delay(500);
    if(s.read() == 180){
      break;
    }
  }
}
void loop(){

 
  s.write(0);
  delay(1000);
  s.write(90);
  delay(1000);
  s.write(180);
  delay(1000);
  s.write(90);
  delay(1000);
  if(s.read() == 0){
    exit(0);
  }
  
}