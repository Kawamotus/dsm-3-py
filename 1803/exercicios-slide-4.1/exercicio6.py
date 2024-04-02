import os
os.system('cls')

matriz = []

for i in range(1, 3):
    linha = []
    matriz.append(linha)
    
    for j in range(1, 4):
        capital = input(f"Digite o nome da capital {i}, {j}: ")
        linha.append(capital)
        
print(matriz)