import serial
from tkinter import *
import time

arduino = serial.Serial('COM8', 9600)

def funcao_botao1():
    global arduino
    arduino.write(b'a')
    label_musica["text"] = "01 - The Simpsons"
#    time.sleep(5)
#    label_musica["text"] = ""
    

def funcao_botao2():
    global arduino
    arduino.write(b'b')
    label_musica["text"] = "02 - Indiana Jones"

def funcao_botao3():
    global arduino
    arduino.write(b'c')
    label_musica["text"] = "03 - Take On Me"

def funcao_botao4():
    global arduino
    arduino.write(b'd')
    label_musica["text"] = "04 - Entertainer"
    
def funcao_botao5():
    global arduino
    arduino.write(b'e')
    label_musica["text"] = "05 - Muppets"

def funcao_botao6():
    global arduino
    arduino.write(b'f')
    label_musica["text"] = "06 - X files"

def funcao_botao7():
    global arduino
    arduino.write(b'g')
    label_musica["text"] = "07 - Looney Tunes"

def funcao_botao8():
    global arduino
    arduino.write(b'h')
    label_musica["text"] = "08 - 20th Century Fox"

def funcao_botao9():
    global arduino
    arduino.write(b'i')
    label_musica["text"] = "09 - James Bond"

def funcao_botao10():
    global arduino
    arduino.write(b'j')
    label_musica["text"] = "10 - MASH"

def funcao_botao11():
    global arduino
    arduino.write(b'k')
    label_musica["text"] = "11 - Star Wars"

def funcao_botao12():
    global arduino
    arduino.write(b'l')
    label_musica["text"] = "12 - Good Bad"

def funcao_botao13():
    global arduino
    arduino.write(b'm')
    label_musica["text"] = "13 - Top Gun"

def funcao_botao14():
    global arduino
    arduino.write(b'n')
    label_musica["text"] = "14 - A-Team"

def funcao_botao15():
    global arduino
    arduino.write(b'o')
    label_musica["text"] = "15 - Flinstones"

def funcao_botao16():
    global arduino
    arduino.write(b'p')
    label_musica["text"] = "16 - Jeopardy"

def funcao_botao17():
    global arduino
    arduino.write(b'q')
    label_musica["text"] = "17 - Gadget"

def funcao_botao18():
    global arduino
    arduino.write(b'r')
    label_musica["text"] = "18 - Smurfs"

def funcao_botao19():
    global arduino
    arduino.write(b's')
    label_musica["text"] = "19 - Mahna Mahna"

def funcao_botao20():
    global arduino
    arduino.write(b't')
    label_musica["text"] = "20 - Leisure Suit"

def funcao_botao21():
    global arduino
    arduino.write(b'u')
    label_musica["text"] = "21 - Mission Impossible"

def funcao_botao22():
    global arduino
    arduino.write(b'v')
    label_musica["text"] = "22 - Doom Level 1"

def funcao_botao23():
    global arduino
    arduino.write(b'w')
    label_musica["text"] = "23 - Zelda Theme"

def funcao_botao24():
    global arduino
    arduino.write(b'x')
    label_musica["text"] = "24 - Ninja Turtles"

def funcao_botao25():
    global arduino
    arduino.write(b'y')
    label_musica["text"] = "25 - Tequila"

def funcao_botao26():
    global arduino
    arduino.write(b'z')
    label_musica["text"] = "26 - Puff"

def funcao_botao27():
    global arduino
    arduino.write(b'A')
    label_musica["text"] = "27 - Ironic"

def funcao_botao28():
    global arduino
    arduino.write(b'B')
    label_musica["text"] = "28 - Like A Virgin"

def funcao_botao29():
    global arduino
    arduino.write(b'C')
    label_musica["text"] = "29 - All Star"

def funcao_botao30():
    global arduino
    arduino.write(b'D')
    label_musica["text"] = "30 - Graduation"

def funcao_botao31():
    global arduino
    arduino.write(b'E')
    label_musica["text"] = "31 - Canon"
    

janela = Tk()
janela.geometry("500x400+0+0")
janela.configure(background="light blue")

label_1 = Label(janela, text="Arduino Play!", font="Arial 10", foreground="black")
label_1.place(x=190, y=5)

label_musica = Label(janela, text="", font="Arial 10", foreground="black")
label_musica.place(x=190, y=30)

botao_1 = Button(janela, width=5, text="01", command=funcao_botao1, background="yellow")
botao_1.place(x=25, y=60)

botao_2 = Button(janela, width=5, text="02", command=funcao_botao2, background="yellow")
botao_2.place(x=25, y=90)

botao_3 = Button(janela, width=5, text="03", command=funcao_botao3, background="yellow")
botao_3.place(x=25, y=120)

botao_4 = Button(janela, width=5, text="04", command=funcao_botao4, background="yellow")
botao_4.place(x=25, y=150)

botao_5 = Button(janela, width=5, text="05", command=funcao_botao5, background="yellow")
botao_5.place(x=25, y=180)

botao_6 = Button(janela, width=5, text="06", command=funcao_botao6, background="yellow")
botao_6.place(x=25, y=210)

botao_7 = Button(janela, width=5, text="07", command=funcao_botao7, background="yellow")
botao_7.place(x=25, y=240)

botao_8 = Button(janela, width=5, text="08", command=funcao_botao8, background="yellow")
botao_8.place(x=25, y=270)

botao_9 = Button(janela, width=5, text="09", command=funcao_botao9, background="yellow")
botao_9.place(x=25, y=300)

botao_10 = Button(janela, width=5, text="10", command=funcao_botao10, background="yellow")
botao_10.place(x=25, y=330)

botao_11 = Button(janela, width=5, text="11", command=funcao_botao11, background="yellow")
botao_11.place(x=220, y=60)

botao_12 = Button(janela, width=5, text="12", command=funcao_botao12, background="yellow")
botao_12.place(x=220, y=90)

botao_13 = Button(janela, width=5, text="13", command=funcao_botao13, background="yellow")
botao_13.place(x=220, y=120)

botao_14 = Button(janela, width=5, text="14", command=funcao_botao14, background="yellow")
botao_14.place(x=220, y=150)

botao_15 = Button(janela, width=5, text="15", command=funcao_botao15, background="yellow")
botao_15.place(x=220, y=180)

botao_16 = Button(janela, width=5, text="16", command=funcao_botao16, background="yellow")
botao_16.place(x=220, y=210)

botao_17 = Button(janela, width=5, text="17", command=funcao_botao17, background="yellow")
botao_17.place(x=220, y=240)

botao_18 = Button(janela, width=5, text="18", command=funcao_botao18, background="yellow")
botao_18.place(x=220, y=270)

botao_19 = Button(janela, width=5, text="19", command=funcao_botao19, background="yellow")
botao_19.place(x=220, y=300)

botao_20 = Button(janela, width=5, text="20", command=funcao_botao20, background="yellow")
botao_20.place(x=220, y=330)

botao_21 = Button(janela, width=5, text="21", command=funcao_botao21, background="yellow")
botao_21.place(x=415, y=60)

botao_22 = Button(janela, width=5, text="22", command=funcao_botao22, background="yellow")
botao_22.place(x=415, y=90)

botao_23 = Button(janela, width=5, text="23", command=funcao_botao23, background="yellow")
botao_23.place(x=415, y=120)

botao_24 = Button(janela, width=5, text="24", command=funcao_botao24, background="yellow")
botao_24.place(x=415, y=150)

botao_25 = Button(janela, width=5, text="25", command=funcao_botao25, background="yellow")
botao_25.place(x=415, y=180)

botao_26 = Button(janela, width=5, text="26", command=funcao_botao26, background="yellow")
botao_26.place(x=415, y=210)

botao_27 = Button(janela, width=5, text="27", command=funcao_botao27, background="yellow")
botao_27.place(x=415, y=240)

botao_28 = Button(janela, width=5, text="28", command=funcao_botao28, background="yellow")
botao_28.place(x=415, y=270)

botao_29 = Button(janela, width=5, text="29", command=funcao_botao29, background="yellow")
botao_29.place(x=415, y=300)

botao_30 = Button(janela, width=5, text="30", command=funcao_botao30, background="yellow")
botao_30.place(x=415, y=330)

botao_31 = Button(janela, width=5, text="31", command=funcao_botao31, background="yellow")
botao_31.place(x=415, y=360)

janela.mainloop()



    
