import os
os.system('cls')

lista = list(range(1,21))
mTres = []

for n in lista:
    if n % 3 == 0:
        print(f"O número {n} é múltiplo de 3! ")
        mTres.append(n)

print(f"A quantidade de números múltiplos de 3 na lista de 1 a 20 é {len(mTres)}")