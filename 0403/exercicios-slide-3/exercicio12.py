import os
os.system('cls')

nome = []
c = 1

for i in range(1, 8):
    n = input(f"Digite o {i}º nome: ")
    nome.append(n)

print("Nomes digitados: ")
for i in nome:
    print(f"O {c}º nome armazenado é {i}")
    c += 1