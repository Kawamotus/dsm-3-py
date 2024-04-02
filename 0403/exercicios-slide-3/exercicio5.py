import os
os.system('cls')

i = 1
j = 0

while i <= 4:
        r1 = input("Digite uma a resposta pra primeira questão('A', 'B', 'C', 'D'): ")
        if r1.upper() == "A":
            j += 1
        
        r2 = input("Digite uma a resposta pra segunda questão('A', 'B', 'C', 'D'): ")
        if r2.upper() == "C":
            j += 1

        r3 = input("Digite uma a resposta pra terceira questão('A', 'B', 'C', 'D'): ")
        if r3.upper() == "D":
            j += 1

        print(f"Jogador {i} - {j} pontos")
        j = 0
        i += 1
