sexo = int(input("Digite o sexo da pessoa: \n0 - Mulher\n1 - Homem\n"))
altura = float(input("Digite a altura da pessoa em m: "))

if sexo == 0:
    pesoIdeal = (62.1*altura) - 44.7
    print(f"O peso ideal dessa pessoa é de: {pesoIdeal:.2f}kg")
elif sexo == 1:
    pesoIdeal = (72.7*altura) - 58
    print(f"O peso ideal dessa pessoa é de: {pesoIdeal:.2f}kg")
else:
    print("Insira valores válidos!!!")