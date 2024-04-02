import os
os.system('cls')

frutas = ["abacate", "laranja", "maçã", "pera"]

for lista in frutas:
    print(lista)

#buscar nome da fruta
busca = input("Digite uma fruta que deseja buscar: ")
for i in frutas:
    print(i)
    if i == busca:
        print(f"Fruta encontrada: {busca}")
        break
    else:
        print(f"A fruta {busca} não foi encontrada")