import os
os.system('cls')

letra = input("Digite uma letra: ")

letra = letra.upper();

match letra:
    case "A":
        print(f"A letra '{letra}' é uma vogal!")
    
    case "E":
        print(f"A letra '{letra}' é uma vogal!")

    case "I":
        print(f"A letra '{letra}' é uma vogal!")
    
    case "O":
        print(f"A letra '{letra}' é uma vogal!")
    
    case "U":
        print(f"A letra '{letra}' é uma vogal!")
    
    case _:
        print(f"A letra '{letra}' não é uma vogal")