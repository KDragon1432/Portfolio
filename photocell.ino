int photocellPin = A0;
int del=100;  
int photocellReading;
int LEDbrightness;
 
void setup(void) {
  for (int i = 10; i<= 12 ; i+= 1) {
    pinMode(i, OUTPUT);
  }
}
 
void loop(void) {

    photocellReading = analogRead(photocellPin);
    LEDbrightness = map(photocellReading, 0, 1023, 0, 255);


    if (photocellReading < 255) {
      for (int i =10 ; i <= 12; i +=1 ) {
        digitalWrite(i, HIGH);
        delay(del);
        digitalWrite(i, LOW);
      }
      for (int i =11 ; i>= 9; i -= 1) {
        digitalWrite(i, HIGH);
        delay(del);
        digitalWrite(i, LOW);
      }
    }
 
    delay(50);
}
