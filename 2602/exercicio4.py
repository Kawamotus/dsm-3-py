numero = int(input("Insira um número inteiro e positivo: "))
par = numero%2

if par == 0:
    r = numero**2
    print(f"O resultado de {numero} ao quadrado é: {r:.2f}")
elif par != 0:
    r = numero**3
    print(f"O resultado de {numero} ao cubo é {r:.2f}")
else:
    print("Valores inseridos incorretamente!!!")