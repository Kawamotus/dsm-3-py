import os
os.system('cls')

print("* ***Lojas Luiz*** *")

i = 1
preco = 2
total = 0

while preco != 0:
    preco = float(input(f"Produto {i}: R$"))
    total += preco
    i += 1

print(f"{'*'*30}")

print(f"Total: R${total}")
dinheiro = float(input("Dinheiro: R$"))
troco = dinheiro - total

if troco < 0:
    print(f"Valor insuficiente faltam R${troco*-1}")
else:
    print(f"Troco: R${troco}")