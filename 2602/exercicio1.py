num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    r = num1/num2
    print(f"O resultado da divisão do maior número pelo menor é: {r:.2f}")
elif num2 > num1:
    r = num2/num1
    print(f"O resultado da divisão do maior número pelo menor é: {r:.2f}")
else:
    print("Os números são iguais! :D")