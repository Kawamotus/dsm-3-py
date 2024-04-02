import os
os.system('cls')

numeros = []
for i in range(1, 11):
    n = int(input(f"Digite o {i}º número: "))
    numeros.append(n)

for i in numeros:
    if i%2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é impar")