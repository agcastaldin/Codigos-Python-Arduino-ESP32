import serial
from tkinter import *

valor_led1 = 1
valor_led2 = 1
valor_led3 = 1
valor_led4 = 1

arduino = serial.Serial('COM6', 9600)

def funcao_botao1():
    global valor_led1
    global arduino

    if valor_led1 == 1:
        valor_led1 = 0
        arduino.write(b'A')
        label_estado_led1["text"] = "Ligado"
        label_estado_led1["foreground"] = "blue"
    else:
        valor_led1 = 1
        arduino.write(b'a')
        label_estado_led1["text"] = "Desligado"
        label_estado_led1["foreground"] = "blue"

def funcao_botao2():
    global valor_led2
    global arduino

    if valor_led2 == 1:
        valor_led2 = 0
        arduino.write(b'C')
        label_estado_led2["text"] = "Ligado"
        label_estado_led2["foreground"] = "blue"
    else:
        valor_led2 = 1
        arduino.write(b'c')
        label_estado_led2["text"] = "Desligado"
        label_estado_led2["foreground"] = "blue"

def funcao_botao3():
    global valor_led3
    global arduino

    if valor_led3 == 1:
        valor_led3 = 0
        arduino.write(b'B')
        label_estado_led3["text"] = "Ligado"
        label_estado_led3["foreground"] = "blue"
    else:
        valor_led3 = 1
        arduino.write(b'b')
        label_estado_led3["text"] = "Desligado"
        label_estado_led3["foreground"] = "blue"

def funcao_botao4():
    global valor_led4
    global arduino

    if valor_led4 == 1:
        valor_led1 = 0
        valor_led2 = 0    
        valor_led3 = 0
        valor_led4 = 0
        arduino.write(b'A,B,C')
        label_estado_led1["text"] = "Ligado"
        label_estado_led1["foreground"] = "blue"
        label_estado_led2["text"] = "Ligado"
        label_estado_led2["foreground"] = "blue"
        label_estado_led3["text"] = "Ligado"
        label_estado_led3["foreground"] = "blue"
        label_estado_led4["text"] = "Ligado"
        label_estado_led4["foreground"] = "blue"
    else:
        valor_led1 = 1
        valor_led2 = 1
        valor_led3 = 1
        valor_led4 = 1
        arduino.write(b'a,b,c')
        label_estado_led1["text"] = "Desligado"
        label_estado_led1["foreground"] = "blue"
        label_estado_led2["text"] = "Desligado"
        label_estado_led2["foreground"] = "blue"
        label_estado_led3["text"] = "Desligado"
        label_estado_led3["foreground"] = "blue"
        label_estado_led4["text"] = "Desligado"
        label_estado_led4["foreground"] = "blue"

janela = Tk()
janela.geometry("500x400+0+0")
janela.configure(background="light blue")

#led vermelho
label_1 = Label(janela, text="LED VERMELHO: ", font="Arial 15", foreground="red")
label_1.place(x=300, y=10)

label_estado_led1 = Label(janela, text="", font="Arial 22")
label_estado_led1.place(x=300, y=40)

botao_1 = Button(janela, width=20, text="ENVIAR", command=funcao_botao1, background="yellow")
botao_1.place(x=300, y=100)

#led verde
label_2 = Label(janela, text="LED VERDE: ", font="Arial 15", foreground="green")
label_2.place(x=50, y=10)

label_estado_led2 = Label(janela, text="", font="Arial 22")
label_estado_led2.place(x=50, y=40)

botao_2 = Button(janela, width=20, text="ENVIAR", command=funcao_botao2, background="yellow")
botao_2.place(x=50, y=100)

#led amarelo
label_3 = Label(janela, text="LED AMARELO: ", font="Arial 15", foreground="yellow")
label_3.place(x=50, y=210)

label_estado_led3 = Label(janela, text="", font="Arial 22")
label_estado_led3.place(x=50, y=240)

botao_3 = Button(janela, width=20, text="ENVIAR", command=funcao_botao3, background="yellow")
botao_3.place(x=50, y=300)

#todos
label_4 = Label(janela, text="TODOS: ", font="Arial 15", foreground="black")
label_4.place(x=300, y=210)

label_estado_led4 = Label(janela, text="", font="Arial 22")
label_estado_led4.place(x=300, y=240)

botao_4 = Button(janela, width=20, text="ENVIAR", command=funcao_botao4, background="yellow")
botao_4.place(x=300, y=300)


janela.mainloop()


'''
codigo utilizado no arduino

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
    
