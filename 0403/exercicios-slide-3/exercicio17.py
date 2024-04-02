import os
os.system('cls')

listaLinguagens = ["python", "c#", "Visual Basic", "C++", "Delphi", "Cobol"]

for i in listaLinguagens:
    if len(i) <= 3:
        continue
    print(f"A linguagem {i} possui mais de 3 caracteres! ")
    
print("\n\n")

for i in listaLinguagens:
    print(f"A linguagem {i} possui {len(i)} caracteres")