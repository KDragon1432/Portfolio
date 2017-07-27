const int buzzerPin = 4;
#include <Servo.h>                      
Servo servoLeft;
Servo servoRight;
int RightWhisker = 7;
int LeftWhisker = 5;
void setup()                                 
{
  pinMode(buzzerPin, OUTPUT);
  tone(4, 3000, 1000);
  delay(1000);
  pinMode(RightWhisker , INPUT);
  pinMode(LeftWhisker , INPUT);
  Serial.begin(9600);
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
         
}  
 
void loop()                                 
{ 


  int wLeft = digitalRead(LeftWhisker);              
  int wRight = digitalRead(RightWhisker);  
  if ((wLeft == 0) and (wRight == 0))
  {tone(buzzerPin, 523, 2000);
    backward(1000);
    turnRight(2000);
  }
  
  else if (wLeft == 0) 
  {tone(buzzerPin, 523, 2000);  
  backward(1000);
  turnRight(1000);}
  else if (wRight == 0)
  {tone(buzzerPin, 523, 2000);
  backward(1000);
  turnLeft(1000);}           
  else 
  {forward(1000);}
 
                        
}


void forward(int times)
{ servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(1000); 
  delay(times);}
void backward(int times) 
{ servoLeft.writeMicroseconds(1000);
  servoRight.writeMicroseconds(2000);
  delay(times);}

void turnLeft(int times)
{ servoLeft.writeMicroseconds(1000);
  servoRight.writeMicroseconds(1000); 
  delay(times);}

void turnRight(int times)
{ servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
  delay(times);
}

void STOP(int times)
{ servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
  delay(times);}



