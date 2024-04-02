import os
os.system('cls')

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Os números são iguais! :D")
    exit()
elif num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número! :D")
    exit()
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número! :D")
    exit()
elif num3 > num1 and num3 > num2:
    print(f"{num3} é o maior número! :D")
    exit()