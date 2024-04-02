import os
os.system('cls')

nivel = int(input("Digite o nível de poluição(números inteiros de 0 à 8): "))

if nivel >= 0 and nivel <= 2:
    op = 1
elif nivel >= 3 and nivel <= 5:
    op = 2
elif nivel >= 6 and nivel <= 7:
    op = 3
elif nivel >= 8:
    op = 4
else:
    op = 0

match op:
    case 1:
        print(f"Nivel de poluição {nivel}:\nAceitável!")

    case 2:
        print(f"Nivel de poluição {nivel}:\nSuspender Atividades Grupo 1")
    
    case 3:
        print(f"Nivel de poluição {nivel}:\nSuspender Atividades Grupo 1 e 2")

    case 4:
        print(f"Nivel de poluição {nivel}:\nSuspender Atividades de todos os grupos")
    
    case 0:
        print("Digite um valor válido!")

    case _:
        print("Digite um valor válido!")