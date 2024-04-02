import os
os.system('cls')

lista = ["python", "c#", "Visual Basic", "C++", "Delphi", "Cobol", "Clipper", "PHP", "Java"]
posicao = 0 #iniciei o contador em 0 considerando a posição vetorial, que se conta partindo o 0, não do 1
busca = input("Digite um nome para buscar na lista: ")

for i in lista:
    if i == busca:
        print(f"Linguagem encontrada: {busca} na posição {posicao}")
        break
    else:
        print(f"Linguagem não encontrada: {busca} na posição {posicao}")

    posicao += 1