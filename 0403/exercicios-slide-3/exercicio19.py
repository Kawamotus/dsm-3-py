import os
os.system('cls')

vogais = ["A", "E", "I", "O", "U"]

for i in range(1, 11):
    verVogal = input("Digite uma letra para verificar se é vogal: ")
    
    if verVogal.upper() in vogais:
        print(f"A letra {verVogal} é uma vogal!")
    else:
        print(f"{verVogal} não é uma vogal :(")