import os
os.system('cls')

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

for i in numeros:
    if i%2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é impar")