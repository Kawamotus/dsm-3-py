from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import pymongo

tela = Tk()
tela.title("Exemplo MongoDB")
tela.geometry("800x600")
tela.resizable(True, True)
tela.configure(background="#fff")

# Criação do Banco no Mongo
exemplo = pymongo.MongoClient("mongodb://localhost:27017/")
db=exemplo["exemplo"]
collection = db["clientes"]

# Interface
lblTitulo = Label(tela, text="Cadastro de Clientes", font=("Arial",30,"bold")).place(x=200, y=50)

lblCodigo = Label(tela, text="Código").place(x=130,y=140)
txtCodigo = Entry(tela, width=20, borderwidth=2,fg="black", bg="white")
txtCodigo.place(x=190,y=140)

lblNome = Label(tela, text="Nome").place(x=130,y=170)
txtNome = Entry(tela, width=20, borderwidth=2,fg="black", bg="white")
txtNome.place(x=190,y=170)

lblCPF = Label(tela, text="CPF").place(x=450,y=140)
txtCPF = Entry(tela, width=20, borderwidth=2,fg="black", bg="white")
txtCPF.place(x=510,y=140)

lblIdade = Label(tela, text="Idade").place(x=130,y=200)
txtIdade = Entry(tela, width=20, borderwidth=2,fg="black", bg="white")
txtIdade.place(x=190,y=200)

lblEndereco = Label(tela, text="Endereço").place(x=450,y=170)
txtEndereco = Entry(tela, width=20, borderwidth=2,fg="black", bg="white")
txtEndereco.place(x=510,y=170)

lblCidade = Label(tela, text="Cidade").place(x=130,y=230)
txtCidade = Entry(tela, width=20, borderwidth=2,fg="black", bg="white")
txtCidade.place(x=190,y=230)

lblEstado = Label(tela, text="Estado").place(x=450,y=200)
cmbEstado = ttk.Combobox(tela, values = ["SP", "RJ", "SC", "AM", "PE", "PB", "MG", "RS", "ES"])
cmbEstado.place(x=510, y=200)

#metodos para o CRUDzinho
#metodo salvar
def salvar():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    cpf = txtCPF.get()
    idade = int(txtIdade.get())
    endereco = txtEndereco.get()
    cidade = txtCidade.get()
    estado = cmbEstado.get()
    
    #limpando caixas de texto/cmbbox
    txtCodigo.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtCPF.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtEndereco.delete(0, tk.END)
    txtIdade.delete(0, tk.END)
    txtCidade.delete(0, tk.END)
    cmbEstado.set("")
    
    #para inserir na coleção clientes
    cliente = {"código": codigo, "nome": nome, "cpf": cpf, "idade": idade, "endereco": endereco, "cidade": cidade, "estado": estado}
    collection.insert_one(cliente)
    messagebox.showinfo("Mensagem", "Cadastrado com sucesso :D")
    
#metodo update
def update():
    codigo = txtCodigo.get()
    nome = txtNome.get()
    cpf = txtCPF.get()
    idade = int(txtIdade.get())
    endereco = txtEndereco.get()
    cidade = txtCidade.get()
    estado = cmbEstado.get()
    
    #para atualizar
    collection.update_one({"código": codigo}, {"$set": {"nome": nome, "cpf": cpf, "idade": idade, "endereco": endereco, "cidade": cidade, "estado": estado}})
    
    messagebox.showinfo("Mensagem", nome + " atualizado com sucesso :D")
    
#metodo excluir
def delete():
    codigo = txtCodigo.get()
    
    #para excluir
    collection.delete_one({"código": codigo})
    messagebox.showinfo("Mensagem", "Deletado com sucesso :D")
    
#metodo consultar
def consultar():
    codigo = txtCodigo.get()
    
    #para consultar
    resultado = collection.find_one({"código": codigo})
    
    if resultado:
        txtNome.insert(END, f"{resultado['nome']}")
        txtCidade.insert(END, f"{resultado['cidade']}")
        txtCPF.insert(END, f"{resultado['cpf']}")
        txtEndereco.insert(END, f"{resultado['endereco']}")
        txtIdade.insert(END, f"{resultado['idade']}")
        cmbEstado.insert(END, f"{resultado['estado']}")
    else:
        lblResultado.config(text="Nenhum resultado encontrado :(")
        
lblResultado = Label(text="")
lblResultado.place(x=600, y=310)

btnSalvar = Button(tela, text="Salvar", width=13, height=13, command=salvar).place(x=130, y=280)
btnAlterar = Button(tela, text="Alterar", width=13, height=13, command=update).place(x=220, y=280)
btnExcluir = Button(tela, text="Excluir", width=13, height=13, command=delete).place(x=310, y=280)
btnConsultar = Button(tela, text="Consultar", width=13, height=13, command=consultar).place(x=400, y=280)

btnSair = Button(tela, text="Sair", width=13, height=13, command=tela.quit).place(x=490, y=280)

tela.mainloop()