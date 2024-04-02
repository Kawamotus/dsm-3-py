import os
os.system('cls')

nomes = ["Luiz","Ana","Cristina","Fernanda","Maria Alice", "Joaquina"]

i = 1

while i != 0:
    i = int(input("1 - Buscar\n0 - Sair\n"))
    if i == 1:
        busca = input("Digite um nome que deseja buscar: ")
        for j in nomes:
            if j == busca:
                print(f"Nome encontrado: {busca}")
                break
            else:
                print(f"{j} =/= {busca} (nome não encontrado)")

    elif i == 0:
        break
    else:
        print("Opção inválida!")