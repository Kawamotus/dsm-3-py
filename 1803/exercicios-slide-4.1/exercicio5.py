import os
os.system('cls')

matriz = []
vetorzao = []
c = 0

for i in range(1, 5):
    linha = []
    matriz.append(linha)
    
    for j in range(1, 5):
        numero = int(input(f"Digite o número para posição {i}, {j}: "))
        linha.append(numero)

for i in matriz:
    for j in i:
        if j > 10:
            vetorzao.append(j)
            c += 1

print(vetorzao)
print(f"A quantidade de números maiores que 10 é: {c}")
