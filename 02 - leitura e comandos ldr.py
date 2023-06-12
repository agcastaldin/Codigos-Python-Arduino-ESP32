import serial
import time

ser = serial.Serial('COM6', 9600)

while True:
    # bloco 1 - recebe os dados via serial
    data = ser.readline().decode().strip()
    print('Valor lido do LDR: ', data)
    #

    ## bloco 2 - valida o valor recebido e
    ## envia comando ao arduino via serial
    ## para acender ou apagar o led
    if int(data) < 400:
        ser.write(b'S') #acende led
        print("Led aceso")
    else:
        ser.write(b's') #apaga led
        print("Led apagado")

'''
Código utilizado no Arduino:

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
'''

    
