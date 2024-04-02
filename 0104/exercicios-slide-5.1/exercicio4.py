from tkinter import *
tela = Tk()

bg = "#451521"

tela.title("Calculo Total Produto")
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

labelNomeProduto = Label(tela,font=fonte, fg=fg, bg=bg, text="Nome do Produto: " ).place(x=10, y=15)
labelQuantidade = Label(tela,font=fonte, fg=fg, bg=bg, text="Quantidade comprada: " ).place(x=10, y=45)
labelPreco = Label(tela,font=fonte, fg=fg, bg=bg, text="Preço: " ).place(x=10, y=75)
labelTotal = Label(tela,font=fonte, fg=fg, bg=bg, text="Total: " ).place(x=10, y=105)

txtNomeProduto = Entry(tela, width=60 , borderwidth=3, fg="black")
txtNomeProduto.place(x=150, y=15)
txtNomeProduto.insert(0,"")

txtQuantidade = Entry(tela, width=20 , borderwidth=3, fg="black")
txtQuantidade.place(x=150, y=45)
txtQuantidade.insert(0,"")

txtPreco = Entry(tela, width=20 , borderwidth=3, fg="black")
txtPreco.place(x=150, y=75)
txtPreco.insert(0,"")

txtTotal = Entry(tela, width=20 , borderwidth=3, fg="black")
txtTotal.place(x=150, y=105)
txtTotal.insert(0,"")

def mostraDados():
    qtd = float(txtQuantidade.get())
    preco = float(txtPreco.get())
    total = qtd * preco
    txtTotal.insert(0, total)
    
    labelDados = Label(tela, font=fonte, fg=fg, bg=bg, text="Produto: " + txtNomeProduto.get() + "\nQuantidade: " + txtQuantidade.get() + "\nPreço: " + txtPreco.get() + "\n\nTotal: " + txtTotal.get())
    labelDados.place(x=200, y=200)
    
btnEnviar = Button(tela,text="Calcular", font="Calibri 10 bold", bg="#1ed", command=mostraDados)
btnEnviar.place(x= 250 , y = 150)

tela.mainloop()