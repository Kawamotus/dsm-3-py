from tkinter import *
tela = Tk()

tela.title("Cadastro de Clientes")
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
labelEmail = Label(tela,font=fonte, fg=fg, bg=bg, text="E-mail: " ).place(x=10, y=45)
labelTelefone = Label(tela,font=fonte, fg=fg, bg=bg, text="Telefone: " ).place(x=10, y=75)
labelEndereco = Label(tela,font=fonte, fg=fg, bg=bg, text="Endereço: " ).place(x=10, y=105)

txtNome = Entry(tela, width=60 , borderwidth=3, fg="black")
txtNome.place(x=85, y=15)
txtNome.insert(0,"")

txtEmail = Entry(tela, width=60 , borderwidth=3, fg="black")
txtEmail.place(x=85, y=45)
txtEmail.insert(0,"")

txtTelefone = Entry(tela, width=60 , borderwidth=3, fg="black")
txtTelefone.place(x=85, y=75)
txtTelefone.insert(0,"")

txtEndereco = Entry(tela, width=60 , borderwidth=3, fg="black")
txtEndereco.place(x=85, y=105)
txtEndereco.insert(0,"")

def mostraDados():
    #mudar fonte e coisas
    labelTitulo = Label(tela, font=fonte, fg=fg, bg=bg, text="Dados do Cliente")
    labelTitulo.place(x=200, y=180)
    labelDados = Label(tela, font="Arial 12", fg="#000", bg="#fff", text="Nome: " + txtNome.get() + "\nEmail: " + txtEmail.get() + "\nTelefone: " + txtTelefone.get() + "\nEndereço: " + txtEndereco.get())
    labelDados.place(x=200, y=200)

btnEnviar = Button(tela,text="Cadastrar", font="Calibri 10 bold", bg="#1ed", command=mostraDados)
btnEnviar.place(x= 250 , y = 150)

tela.mainloop()