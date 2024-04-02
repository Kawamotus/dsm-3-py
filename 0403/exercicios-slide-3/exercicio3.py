import os
os.system('cls')

tab = int(input("Digite um número inteiro para ser feita a tabuada: "))
i = 1

print(f"Tabuada do: {tab}")

while i <= 10:
    r = tab*i
    print(f"{tab} x {i} = {r}")
    i += 1