When the distance sensor from vex detects, input is given and light is turned on
int switchstate = 0;

void setup() {
  pinMode(3, OUTPUT);
  pinMode(2, INPUT);
}

void loop() {

  switchstate = digitalRead(2);

  if (switchstate == LOW) 
  {
    digitalWrite(3, LOW); 
  }

  else 
  {
    digitalWrite(3, HIGH);  
  }
}
