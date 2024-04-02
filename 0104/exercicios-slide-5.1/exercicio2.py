from tkinter import *
tela = Tk()

bg = "#11AACC"

tela.title("Calculo Soma")
largura = 720
altura = 600
tela.configure(background=bg)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 -altura/2
tela.geometry("%dx%d+%d+%d"%(largura,altura,posx,posy))
tela.geometry("720x300")
tela.resizable(True,True)
tela.maxsize(width=800,height=700)
tela.minsize(width=500, height=300)


fonte = "Calibri 10 bold italic"
fg = "#fff"

labelN1 = Label(tela,font=fonte, fg=fg, bg=bg, text="Primeiro número: " ).place(x=10, y=15)
labelN2 = Label(tela,font=fonte, fg=fg, bg=bg, text="Segundo número: " ).place(x=10, y=45)
labelResultado = Label(tela,font=fonte, fg=fg, bg=bg, text="Resultado: " ).place(x=10, y=105)

txtN1 = Entry(tela, width=60 , borderwidth=3, fg="black")
txtN1.place(x=135, y=15)
txtN1.insert(0,"")

txtN2 = Entry(tela, width=60 , borderwidth=3, fg="black")
txtN2.place(x=135, y=45)
txtN2.insert(0,"")

txtResultado = Entry(tela, width=60, borderwidth=3, fg="black")
txtResultado.place(x=135, y=105)
txtResultado.insert(0,"")

def mostraDados():
    n1 = float(txtN1.get())
    n2 = float(txtN2.get())
    total = n1+n2
    txtResultado.insert(0, total)
    labelDados = Label(tela, font=fonte, fg="#000", bg="#fff", text="Resultado: " + txtResultado.get())
    labelDados.place(x=200, y=180)

btnEnviar = Button(tela,text="Calcular", font="Calibri 10 bold", bg="#1ed", command=mostraDados)
btnEnviar.place(x= 250 , y = 150)

tela.mainloop()