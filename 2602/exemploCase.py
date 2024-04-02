import os
os.system('cls')

op = int(input("Escolha a opção: \n1 - Sacar\n2 - Extrato\n3 - Sair\n"))

match op:
    case 1:
        print("Sacar")
        valor = float(input("Digite o valor a sacar em R$: "))
        print(f"Valor retirado: {valor}")
    case 2:
        print("Extrato")
        dias = int(input("Digite a quantidade de dias do extrato: "))
        print(f"retirando o extrado de {dias} dias")
    case 3:
        print("Sair")
        exit()
    case _ :
        print("Opção inválida :(")