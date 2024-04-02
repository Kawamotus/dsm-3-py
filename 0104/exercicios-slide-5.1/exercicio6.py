from tkinter import *
tela = Tk()

bg = "#BA2133"

tela.title("Velocidade Carro")
largura = 720
altura = 600
tela.configure(background=bg)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 -altura/2
tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
tela.geometry("720x400")
tela.resizable(True,True)
tela.maxsize(width=800,height=700)
tela.minsize(width=500, height=300)


fonte = "Calibri 10 bold italic"
fg = "#fff"

labelNomeCarro = Label(tela,font=fonte, fg=fg, bg=bg, text="Nome: " ).place(x=10, y=15)
labelDistancia = Label(tela,font=fonte, fg=fg, bg=bg, text="Distância (m): " ).place(x=10, y=45)
labelTempo = Label(tela,font=fonte, fg=fg, bg=bg, text="Tempo (s): " ).place(x=10, y=75)
labelVelocidade = Label(tela,font=fonte, fg=fg, bg=bg, text="Velocidade (m/s): " ).place(x=10, y=135)

txtNomeCarro = Entry(tela, width=60, borderwidth=3, fg="#000")
txtNomeCarro.place(x=125, y=15)
txtNomeCarro.insert(0, "")

txtDistancia = Entry(tela, width=60, borderwidth=3, fg="#000")
txtDistancia.place(x=125, y=45)
txtDistancia.insert(0, "")

txtTempo = Entry(tela, width=60, borderwidth=3, fg="#000")
txtTempo.place(x=125, y=75)
txtTempo.insert(0, "")

txtVelocidade = Entry(tela, width=60, borderwidth=3, fg="#000")
txtVelocidade.place(x=125, y=135)
txtVelocidade.insert(0, "")

def mostraDados():
    distancia = float(txtDistancia.get())
    tempo = float(txtTempo.get())
    velocidade = distancia/tempo
    txtVelocidade.insert(0, velocidade)
    labelDados = Label(tela, font=fonte, fg=fg, bg=bg, text="O carro " + txtNomeCarro.get() + "\npercorreu " + txtDistancia.get() + "m\nem um tempo de " + txtTempo.get() + "segundos\n\nem uma velocidade de " + txtVelocidade.get() + "m/s")
    labelDados.place(x=200, y=240)
    
btnEnviar = Button(tela,text="Calcular", font=fonte, bg="#1ed", command=mostraDados)
btnEnviar.place(x= 250 , y = 200)

tela.mainloop()