import os
os.system('cls')

print("Calculadora de aumento salarial :P")

salarioAtual = float(input("Digite o salário atual do funcionário (em R$): "))
categoria = input("Digite a categoria do funcionário(A, B ou C): ")

categoria = categoria.upper()

match categoria:
    case "A":
        salarioFinal = salarioAtual * 1.1
        print(f"Aumento salarial da categoria {categoria}:\nDe R${salarioAtual} para R${salarioFinal}")
    case "B":
        salarioFinal = salarioAtual * 1.15
        print(f"Aumento salarial da categoria {categoria}:\nDe R${salarioAtual} para R${salarioFinal}")
    case "C":
        salarioFinal = salarioAtual * 1.25
        print(f"Aumento salarial da categoria {categoria}:\nDe R${salarioAtual} para R${salarioFinal}")
    case _:
        print("Opção inválida!")