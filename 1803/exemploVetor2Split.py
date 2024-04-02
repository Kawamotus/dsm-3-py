import os
os.system('cls')

#exemplo vetor sem definição de tamanho usando split

entrada_dados = input("Digite os elementos do vetor separados por espaços: ")
vetor = [int (x) for x in entrada_dados.split()]

print(vetor)