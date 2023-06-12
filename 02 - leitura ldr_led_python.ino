int ldr = A0;
int valorldr = 0;
int led = 10;

void setup() { 
  pinMode(ldr, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
} 

void loop() { 
  valorldr = analogRead(ldr);
  Serial.println(valorldr);
  delay(500);

  while(Serial.available() > 0) { 
    char comando = Serial.read(); 
    if (comando == 'S'){
      digitalWrite(led, HIGH);
    }
    if (comando == 's'){
      digitalWrite(led, LOW);
    }
  }
}
