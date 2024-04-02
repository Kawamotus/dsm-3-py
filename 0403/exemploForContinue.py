import os
os.system('cls')

nomes = ["jose", "maria julia", "luiz", "ana", "fernanda"]

for i in nomes:
    if len(i) != 3:
        continue
    print(f"Olá {i}")

    if i == "luiz":
        print(f"{i}")
        break