import os
os.system('cls')

print("Panificadora Pão de Ontem - Tabela de Preços")

p = 0.54

for i in range(2, 51, 2):
    r = i*p
    print(f"{i} - R${r:.2f}")