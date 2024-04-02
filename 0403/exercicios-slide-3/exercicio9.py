import os
os.system('cls')

nomes = ["Maria", "João", "Paulo", "Magali"]

busca = input("Digite o nome que deseja buscar: ")

for i in nomes:
    if i == busca:
        print(f"Nome encontrado: {busca}")
        break
    else:
        print(f"{i} =/= {busca}")