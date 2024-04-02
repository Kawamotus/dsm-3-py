num1 = float(input("Digite um número positivo: "))
num2 = float(input("Digite outro número positivo: "))

menu = int(input("1 Média ponderada, com pesos 2 e 3, respectivamente\n2. Quadrado da soma dos 2 números\n3. Cubo do menor número \nEscolha uma opção: "))

if menu == 1:
    r = (num1*2 + num2*3)/5
    print(f"O resultado da média ponderada é: {r}")
elif menu == 2:
    r = (num1+num2)**2
    print(f"O resultado do quadrado da soma dos dois números é: {r}")
elif menu == 3:
    if num1 > num2:
        r = num2**3
        print(f"O cubo do menor número é: {r}")
    elif num2 > num1:
        r = num1**3
        print(f"O cubo do menor número é: {r}")
    else:
        print("Os números são iguais :(")
else:
    print("Digite um valor válido!!!")