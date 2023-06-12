import serial
import time ## utilizado no delay
import random ## utilizando no efeito randômico

porta = "COM6"
velocidade = 9600
comand = serial.Serial(porta, velocidade)

#Estrutura de decisão
while True:
    time.sleep(1)
    opcao= input("\nEscolha o comando:           \
                 \nA,a - led A - Vermelho        \
                 \nB,b - led B - Amarelo         \
                 \nC,c - led C - Verde           \
                 \nD,d - todos                   \
                 \nE,e - Sequencial com tempo \
                 \nF - Acendimento Randômico \n\n")
                

    if opcao == "A":
        comand.write(b'A')
        print("Led A aceso")

    if opcao == "a":
        comand.write(b'a')
        print("Led A apagado")

    if opcao == "B":
        comand.write(b'B')
        print("Led B aceso")

    if opcao == "b":
        comand.write(b'b')
        print("Led B apagado")

    if opcao== "C":
        comand.write(b'C')
        print("Led C aceso")

    if opcao== "c":
        comand.write(b'c')
        print("Led c apagado")

    ##### Código complementar acende todos
    if opcao== "D": 
        comand.write(b'A,B,C')
        print("Todos acessos")

    ##### Código complementar apaga todos
    if opcao== "d":
        comand.write(b'a,b,c')
        print("Todos apagados")

    ##### Código complementar acende todos em sequência
    if opcao== "E":
        print("acendendo led A")
        comand.write(b'A')
        time.sleep(1)
        print("acendendo led B")
        comand.write(b'B')
        time.sleep(1)
        print("acendendo led C")
        comand.write(b'C')
        time.sleep(1)
        print("Todos acessos")

    ##### Código complementar apaga todos em sequência
    if opcao== "e":
        print("apagando led A")
        comand.write(b'a')
        time.sleep(1)
        print("apagando led B")
        comand.write(b'b')
        time.sleep(1)
        print("apagando led C")
        comand.write(b'c')
        time.sleep(1)
        print("Todos apagados")

    ##### Código complementar acende todos em sequência randômica e depois apaga
    if opcao== "F":

        sequencia = ["A", "B", "C"]
        sequencia_sorteio = random.sample(sequencia, k=len(sequencia))
        

        print("Calculando ordem de acionamento")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        
        print(sequencia_sorteio)
        time.sleep(1)

        for i in range(0,3):
            print("acendendo led ", sequencia_sorteio[i])
            if sequencia_sorteio[i] == "A":
                comand.write(b'A')
            if sequencia_sorteio[i] == "B":
                comand.write(b'B')
            if sequencia_sorteio[i] == "C":
                comand.write(b'C')
            time.sleep(2)

        for i in range(3, 0, -1):
            print("Apagando em ", i ," s")
            time.sleep(1)

        comand.write(b'a,b,c')
        print("Todos apagados")





'''
código utilizado no Arduino:

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

'''
