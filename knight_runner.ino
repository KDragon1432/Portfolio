int del=100; 
void setup() {
 
  for (int i = 1; i<=14 ; i += 2) {
    pinMode(i, OUTPUT);
  } 
} 
 
void loop() {
  for (int i = 1; i<=14; i += 2) { 
    digitalWrite(i, HIGH);
    delay(del);
    digitalWrite(i, LOW);
  }
  for (int i = 13; i>=0; i -= 2) { 
    digitalWrite(i, HIGH);
    delay(del);
    digitalWrite(i, LOW);
  }
}
