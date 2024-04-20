from tkinter import *
#from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import sys


#criação tela
tela = Tk()
#define icone

tela.title("Controle de gastos")
tela.configure(background='#1e3743')
largura = 900
altura = 420

#tamanho da tela
tela.geometry("900x420")
tela.resizable(True,True)

tela.maxsize(width=1080,height=700)
tela.minsize(width=500, height=300)

# Função sair
def sair():
    sys.exit()

lbl_codigo = Label(tela, text="Código: ", fg='#fff', bg='#1e3743').place(x=40, y= 15)
txt_codigo = Entry(tela, width = 20, borderwidth= 3,fg="blue")
txt_codigo.place(x= 100 , y = 15)
txt_codigo.insert(0,"")

lbl_nome = Label(tela,font="Arial 10 bold italic",text="Nome: ",fg='#fff',bg='#1e3743').place(x= 40 , y= 50)
txt_nome = Entry(tela, width= 70 , borderwidth= 3, fg="blue")
txt_nome.place(x= 100 , y = 50)
txt_nome.insert(0,"")

lbl_idade = Label(tela,font="Arial 10 bold italic",text="Idade: ",fg='#fff',bg='#1e3743').place(x= 550 , y= 50)
txt_idade = Entry(tela, width= 15 , borderwidth= 3, fg="blue")
txt_idade.place(x= 600 , y = 50)
txt_idade.insert(0,"")


# RadioButton
var = StringVar() #intVar se for inteiro
var.set("m") #Como o radiobutton começa

lbl_sexo = Label(tela, font="Arial 10 bold italic", text="Sexo: ", fg="#fff", bg='#1e3743').place(x= 40, y=85)
rdb_buttonm = Radiobutton(tela,text="M", variable=var, value ="m").place(x=100, y=85)
rdb_buttonf = Radiobutton(tela,text="F", variable=var, value ="f").place(x=150, y=85)

lbl_altura = Label(tela,font="Arial 10 bold italic",text="Altura: ",fg='#fff',bg='#1e3743').place(x= 200 , y= 85)
txt_altura = Entry(tela, width= 15 , borderwidth= 3, fg="blue")
txt_altura.place(x= 260 , y = 85)
txt_altura.insert(0,"")

lbl_peso = Label(tela,font="Arial 10 bold italic",text="Peso: ",fg='#fff',bg='#1e3743').place(x= 380 , y= 85)
txt_peso = Entry(tela, width= 15 , borderwidth= 3, fg="blue")
txt_peso.place(x= 430 , y = 85)
txt_peso.insert(0,"")

lbl_dataNasc = Label(tela,font="Arial 10 bold italic", text="Data Nascimento: ",fg='#fff', bg='#1e3743').place(x= 40 , y= 120)
txt_dataNasc = Entry(tela, width= 30 , borderwidth= 3, fg="blue")
txt_dataNasc.place(x= 170 , y = 120)
txt_dataNasc.insert(0,"")

lbl_dataCad = Label(tela,font="Arial 10 bold italic", text="Data de Cadastro: ",fg='#fff', bg='#1e3743').place(x= 380 , y= 120)
txt_dataCad = Entry(tela, width= 30 , borderwidth= 3, fg="blue")
txt_dataCad.place(x= 510 , y = 120)
txt_dataCad.insert(0,"")

lbl_cidade = Label(tela,font="Arial 10 bold italic", text="Cidade: ",fg='#fff', bg='#1e3743').place(x= 380 , y= 155)
combo = ttk.Combobox(tela)
combo['values']= ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati")
combo.current(2)  # define o item selecionado
combo.place(x=440, y=155)

lbl_dataAtt = Label(tela,font="Arial 10 bold italic", text="Data Atualização: ",fg='#fff', bg='#1e3743').place(x= 40 , y= 155)
txt_dataAtt = Entry(tela, width= 30 , borderwidth= 3, fg="blue")
txt_dataAtt.place(x= 170 , y = 155)
txt_dataAtt.insert(0,"")

lbl_descricao = Label(tela,font="Arial 10 bold italic", text="Descriçao: ",fg='#fff', bg='#1e3743').place(x= 40 , y= 190)
txt_descricao = Entry(tela, width= 86 , borderwidth= 3, fg="blue")
txt_descricao.place(x= 170 , y = 190)
txt_descricao.insert(0,"")



#foto_salvar = PhotoImage(file = r"icones\salvar.png")
# foto_excluir = PhotoImage(file = r"icones\excluir.png")
# foto_alterar = PhotoImage(file = r"icones\alterar.png")
# foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

# btn_salvar =  Button(tela, text="Salvar", image= foto_salvar ,compound= TOP ).place(x=170,y=230)  
# btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound=TOP).place(x=230,y=230)
# btn_alterar =  Button(tela, text="Alterar", image= foto_alterar ,compound= TOP ).place(x=290,y=230)  
# btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP).place(x=350,y=230)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair).place(x=620,y=230)

#Imagem

pasta_inicial = ""


def escolher_imagem():

    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha a imagem...",
                                                filetypes=(("Arquivos de Imagem", "*.jpg;*.jpeg;*.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura/proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))

    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=750, y=50)

btn_escolher = Button(tela, text ="Escolher Imagem" , command=escolher_imagem)
btn_escolher.place(x=750,y=190)

lbl_codRes = Label(tela,font="Arial 10", text="Código ",fg='#fff', bg='#1e3743').place(x= 20 , y= 330)
lbl_nomeRes = Label(tela,font="Arial 10", text="Nome",fg='#fff', bg='#1e3743').place(x= 70 , y= 330)
lbl_idadeRes = Label(tela,font="Arial 10", text="Idade",fg='#fff', bg='#1e3743').place(x= 20 , y= 350)
lbl_sexoRes = Label(tela,font="Arial 10", text="Sexo",fg='#fff', bg='#1e3743').place(x= 70 , y= 350)
lbl_altRes = Label(tela,font="Arial 10", text="Altura ",fg='#fff', bg='#1e3743').place(x= 20 , y= 370)
lbl_pesoRes = Label(tela,font="Arial 10", text="Peso",fg='#fff', bg='#1e3743').place(x= 70 , y= 370)
lbl_cidadeRes = Label(tela,font="Arial 10", text="Cidade",fg='#fff', bg='#1e3743').place(x= 20 , y= 390)
lbl_dtnascRes = Label(tela,font="Arial 10", text="Data nascimento",fg='#fff', bg='#1e3743').place(x= 70 , y= 390)

tela.mainloop()