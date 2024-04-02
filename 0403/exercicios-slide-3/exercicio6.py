import os
os.system('cls')

print("Lojas Quase Dois - Tabela de Preços")

i = 1
p = 1.99

for i in range(1, 51):
    r = i*p
    print(f"{i} - R${r}")