import os
os.system('cls')

numero = input("Digite os números separados por espaços: ")
vetor = [int (x) for x in numero.split()]

vetorzao = []

for i in vetor:
    if i%2 == 0:
        vetorzao.append(i)
        

print(f"Os números armazenados são: {vetor}")
print(f"Os números pares são: {vetorzao}")