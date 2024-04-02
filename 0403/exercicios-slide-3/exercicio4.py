import os
os.system('cls')

tab = int(input("Digite um número inteiro para ser feita a tabuada: "))
inicio = int(input("Digite um número inteiro para iniciar a tabuada: "))
limitador = int(input("Digite um número inteiro para encerrar a tabuada: "))

print(f"Tabuada do: {tab}")
print(f"Início: {inicio}")
print(f"Fim: {limitador}")

while inicio <= limitador:
    r = tab*inicio
    print(f"{tab} x {inicio} = {r}")
    inicio += 1