int led1 = 12; 
int led2 = 10; 
int led3 = 8; 

void setup() { 
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT); 
  pinMode(led3, OUTPUT); 
  Serial.begin(9600); 
} 

void loop() { 
  while(Serial.available() > 0) { 
    char comando = Serial.read(); 
    if(comando == 'A') { 
      digitalWrite(led1, HIGH);
    } 
    if(comando == 'a') { 
      digitalWrite(led1, LOW);
    } 
    if(comando == 'B') { 
      digitalWrite(led2, HIGH);
    } 
    if(comando == 'b') { 
      digitalWrite(led2, LOW);
    } 
    if(comando == 'C') { 
      digitalWrite(led3, HIGH);
    } 
    if(comando == 'c') { 
      digitalWrite(led3, LOW); 
    }
   
  } 
}
