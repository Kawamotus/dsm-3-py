import os
os.system('cls')

print("Calculadora de peso em outros planetas! ;D")

peso = float(input("Digite o peso da pessoa na Terra(em kg): "))
planet = int(input("Escolha um planeta para calcular o peso: \n1 - Mercúrio \n2 - Vênus \n3 - Marte \n4 - Júpiter \n5 - Saturno\n"))

match planet:
    case 1:
        pesoFinal = peso * 0.37
        print(f"O peso da pessoa na Terra é de {peso}kg e em Mercúrio é: {pesoFinal:.3f}kg")
    case 2:
        pesoFinal = peso * 0.88
        print(f"O peso da pessoa na Terra é de {peso}kg e em Vênus é: {pesoFinal:.3f}kg")
    case 3:
        pesoFinal = peso * 0.38
        print(f"O peso da pessoa na Terra é de {peso}kg e em Marte é: {pesoFinal:.3f}kg")
    case 4:
        pesoFinal = peso * 2.64
        print(f"O peso da pessoa na Terra é de {peso}kg e em Júpiter é: {pesoFinal:.3f}kg")
    case 5:
        pesoFinal = peso * 1.15
        print(f"O peso da pessoa na Terra é de {peso}kg e em Saturno é: {pesoFinal:.3f}kg")
    
    case _:
        print("Opção inválida!")