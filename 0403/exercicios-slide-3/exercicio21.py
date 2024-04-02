import os
os.system('cls')

i = 1
nomeArrM = []
nomeArrF = []

print("Verificação da necessidade de exame!\n")

while i <= 15:
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo do(a) funcionário(a) - 'F' para feminino e 'M' para masculino: ")
    sexo = sexo.upper()

    if sexo == "M":
        print(f"O funcionário {nome} precisa fazer o exame!")
        nomeArrM.append(nome)
    elif sexo == "F":
        print(f"A funcionária {nome} não precisa fazer o exame! ")
        nomeArrF.append(nome)
    else:
        print(f"{sexo} não é um valor correto! ")

    print("\n")

    i += 1
    

print("\n\n")
print("Precisam realizar o exame: ")
for j in nomeArrM:
    print(f"{j}")

print("\n")
print("Não precisam realizar o exame: ")
for j in nomeArrF:
    print(f"{j}")