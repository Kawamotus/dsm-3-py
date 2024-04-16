from tkinter import *
tela = Tk()

tela.title("Fatec Registro")
largura = 720
altura = 600
tela.configure(background='#1e3743')
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
bg = "#1e3743"

labelNome = Label(tela,font=fonte, fg=fg, bg=bg, text="Nome: " ).place(x=10, y=15)
labelTelefone = Label(tela,font=fonte, fg=fg, bg=bg, text="Telefone: " ).place(x=10, y=35)
labelEndereco = Label(tela,font=fonte, fg=fg, bg=bg, text="Endereço: " ).place(x=10, y=75)
labelCidade = Label(tela,font=fonte, fg=fg, bg=bg, text="Cidade: " ).place(x=10, y=105)

txtNome = Entry(tela, width=60 , borderwidth=3, fg="black")
txtNome.place(x=120, y=15)
txtNome.insert(0,"")

txtTelefone = Entry(tela, width=60 , borderwidth=3, fg="black")
txtTelefone.place(x=120, y=45)
txtTelefone.insert(0,"")

txtEndereco = Entry(tela, width=60 , borderwidth=3, fg="black")
txtEndereco.place(x=120, y=75)
txtEndereco.insert(0,"")

txtCidade = Entry(tela, width=60 , borderwidth=3, fg="black")
txtCidade.place(x=120, y=105)
txtCidade.insert(0,"")

def mostraDados():
    labelDados = Label(tela, font=fonte, fg=fg, bg=bg, text="Nome: " + txtNome.get() + "\nTelefone: " + txtTelefone.get() + "\nEndereço: " + txtEndereco.get() + "\nCidade: " + txtCidade.get())