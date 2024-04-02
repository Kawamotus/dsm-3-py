from tkinter import *

#criacao tela
tela = Tk()

#muda o iconezinho
tela.iconbitmap("C:/Users/kawamotus/Downloads/logo.ico")

#titulo tela
tela.title("Título da tela :D")

#cor da tela
tela.configure(background='red')

#dimensoes da tela
largura = 600
altura = 600

#resolucao do sistema
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

print(largura_screen, altura_screen)

#tamanho da tela
#tela.geometry("600x600")
tela.geometry(largura, altura, posx, posy)

#definir tamanho maximo e minimo (limite)
#tela.resizable(False, False) #nao permite resize

#deixar tela.resizable(True, True) para funcionar
#define tamanho máximo
#tela.maxsize(width=800, height=800)

#define tamanho minimo
#tela.maxsize(width=500, height=300)

#colocando label
lbl_nome = Label(tela, font='Arial 15 bold ', text="Nome: ", fg="white", bg="red").place(x=40, y=40) #medida em px
lbl_cpf = Label(tela, font='Arial 15 bold italic', text='CPF: ', fg="white", bg="red").place(x=40, y=70)

#colocando caixa de texto
txt_nome = Entry(tela, width=60, borderwidth=3, fg='#000') #o .place poderia ser colocado aqq
txt_nome.place(x = 110, y=40)
txt_nome.insert(0, "Digite seu nome")

txt_cpf = Entry(tela, width=60, borderwidth=3, fg='#000', font="Arial 9 italic") #o .place poderia ser colocado aqq
txt_cpf.place(x = 110, y=70)
txt_cpf.insert(0, "Digite seu CPF")

#funcao mostradados
def mostraDados():
    lbl_titulo = Label(tela, text="Dados pessoa", font='Arial 20 italic')
    lbl_titulo.place(x=400, y=300)
    lbl_dados = Label(tela,font="Arial 30 bold", text="Nome: " + txt_nome.get() + "\nCPF: " + txt_cpf.get())
    lbl_dados.place(x=500, y=400)
    
#funcao verificaFocusCaixa
def verificaFocusCaixa(event):
    txt_nome.delete(0, END)
    txt_cpf.delete(0, END)

#botao
btn_botao = Button(tela, text='Cadastrar', font="Arial 10 bold", bg="#1ed", command=mostraDados)
btn_botao.place(x=300, y=300)

#limpar caixa de texto
txt_nome.bind("<FocusIn>", verificaFocusCaixa)
txt_nome.bind("<FocusIn>", verificaFocusCaixa)

tela.mainloop()

