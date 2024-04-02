import os
os.system('cls')

vetor = []

for i in range(1, 6):
    cor = input(f"Digite a {i}º cor: ")
    vetor.append(cor)
    
print(f"As cores são {vetor}")