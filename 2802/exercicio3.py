import os
os.system('cls')

print("Cálculo de Grandezas Elétricas :O")

u = float(input("Digite a tensão (em V): "))
r = float(input("Digie a resistência (em Ώ): "))
i = float(input("Digite a corrente (em A): "))

op = int(input("Escolha uma opção:\n1 - Tensão (em Volt)\n2 - Resistência (em Ohm)\n3 - Corrente (em Ampére)\n0 - Sair\n"))

match op:
    case 0:
        exit()
    case 1:
        u = r*i
        print(f"A tensão é: {u:.2f} V")
    case 2:
        r = u/i
        print(f"A resistência é: {r:.2f} Ohm")
    case 3:
        i = u/r
        print(f"A corrente é: {i:.2f} A")
    