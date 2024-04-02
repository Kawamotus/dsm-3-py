import os
os.system('cls')

matriz = []

for i in range(1, 3):
    linha = []
    matriz.append(linha)
    
    for j in range(1, 6):
        if i <= 1:
            produto = input(f"Digite o nome do produto {j}: ")
            linha.append(produto)
        elif i >= 2:
            quantidade = input(f"Digite a quantidade do produto {j}: ")
            linha.append(quantidade)
        
print(matriz)
