from tkinter import *
tela = Tk()

bg = "#134ABD"

tela.title("Calculo Média")
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


labelN1 = Label(tela,font=fonte, fg=fg, bg=bg, text="1º Nota: " ).place(x=10, y=15)
labelN2 = Label(tela,font=fonte, fg=fg, bg=bg, text="2º Nota: " ).place(x=10, y=45)
labelN3 = Label(tela,font=fonte, fg=fg, bg=bg, text="3º Nota: " ).place(x=10, y=75)
labelResultado = Label(tela,font=fonte, fg=fg, bg=bg, text="Resultado: " ).place(x=10, y=105)

txtN1 = Entry(tela, width=60 , borderwidth=3, fg="black")
txtN1.place(x=135, y=15)
txtN1.insert(0,"")

txtN2 = Entry(tela, width=60 , borderwidth=3, fg="black")
txtN2.place(x=135, y=45)
txtN2.insert(0,"")

txtN3 = Entry(tela, width=60 , borderwidth=3, fg="black")
txtN3.place(x=135, y=75)
txtN3.insert(0,"")

txtResultado = Entry(tela, width=60, borderwidth=3, fg="black")
txtResultado.place(x=135, y=105)
txtResultado.insert(0,"")

def mostraDados():
    n1 = float(txtN1.get())
    n2 = float(txtN2.get())
    n3 = float(txtN3.get())
    total = (n1+n2+n3)/3
    txtResultado.insert(0, total)
    
    if total >= 7:
        situacao = "Aprovado"
    elif total >= 3 and total <= 7:
        situacao = "Exame"
    elif total < 3:
        situacao = "Reprovado"
    
    labelDados = Label(tela, font=fonte, fg=fg, bg=bg, text="Resultado: " + txtResultado.get() + "\n" + situacao)
    labelDados.place(x=200, y=180)
    
btnEnviar = Button(tela,text="Calcular", font="Calibri 10 bold", bg="#1ed", command=mostraDados)
btnEnviar.place(x= 250 , y = 150)

tela.mainloop()