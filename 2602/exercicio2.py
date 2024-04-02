nome1 = input("Digite o nome de uma das pessoas: ")
peso1 = float(input("Digite o peso da pessoa em kg: "))
nome2 = input("Digite o nome da outra pessoa: ")
peso2 = float(input("Digite o peso da pessoa em kg: "))

if peso1 == peso2:
    print(f"{nome1} e {nome2} tem o mesmo peso!")
elif peso1 > peso2:
    print(f"{nome1} é a pessoa mais pesada! ")
elif peso2 > peso1:
    print(f"{nome2} é a pessoa mais pesada! ")