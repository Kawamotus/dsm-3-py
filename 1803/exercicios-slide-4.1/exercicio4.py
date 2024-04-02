import os
os.system('cls')

matriz = []

for i in range(1, 6):
    linha = []
    matriz.append(linha)
    
    for j in range(1, 3):
        numero = int(input(f"Digite o número para posição {i}, {j}: "))
        linha.append(numero)
        
for i in matriz:
    print(i)