from tkinter import *

tela = Tk()
tela.title("open file")
tela.geometry("300x300")

def mostrar():
    Label(tela, text=var.get()).pack()

var = StringVar()
# var = IntVar()

chk_button = Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="Off")
chk_button.deselect() # Define se o check box irá inicializar selecionado ou não
chk_button.pack()

Button(tela, text="Mostrar", command=mostrar).pack()

tela.mainloop()

