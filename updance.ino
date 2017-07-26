const int buzzerPin = 9;
const int songLength = 21;
char notes[] = "fafedfdcdfdcdagdaggfd";
int beats[] = {1,1,1,4,1,1,1,2,1,1,1,2,1,2,2,1,2,1,1,2,4}; 
int tempo = 133;

#include <Servo.h>                      
Servo servoLeft;
Servo servoRight;

void setup()                                 
{
  pinMode(buzzerPin, OUTPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
         
}  
 
void loop()                                 
{       
 
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(1000);
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(1000);
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(1000);
  music();
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
  servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(2000);
  servoLeft.writeMicroseconds(2000);
  music(); 


                        
}


//void forward()
//{ servoLeft.writeMicroseconds(2000);
//  servoRight.writeMicroseconds(1000); }
//void backward() 
//{ servoLeft.writeMicroseconds(1000);
//  servoRight.writeMicroseconds(2000); }

//void turnLeft()
//{ servoLeft.writeMicroseconds(1000);
//  servoRight.writeMicroseconds(1000); }

//void turnRight()
//{ servoLeft.writeMicroseconds(2000);
//  servoRight.writeMicroseconds(2000);
//}
void music(){
  int i, duration;

  for (i = 0; i < songLength; i++)
  {
    duration = beats[i] * tempo;
    if (notes[i] == ' ')           
      {delay(duration);}
    else                          
      {tone(buzzerPin, frequency(notes[i]), duration);
      delay(duration);}
     delay(tempo/10);
  }
  }

int frequency(char note) 
{
  int i;
  const int numNotes = 8;  // number of notes we're storing
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int frequencies[] = {262, 294, 330, 349, 392, 440, 494, 523};
  for (i = 0; i < numNotes; i++) 
  {
    if (names[i] == note)    
    {
      return(frequencies[i]);  
    }
  }
  return(0);
            
}

