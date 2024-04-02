import os
os.system('cls')

print(f"{':D '*3}{'Programa empréstimo:'} {':D '*3}")
#print(f"{'Programão ' * 6784398274983274983274}")

print("Responda \n1 - Sim\n0 - Não")

negativado = int(input("Possui nome negativado? "))
if negativado == 1:
    print("Você não pode realizar o empréstimo!")
elif negativado == 0:
    carteiraAssinada = int(input("Possui carteira assinada? "))
    if carteiraAssinada == 0:
        print("Não pode realizar o empréstimo")
    elif carteiraAssinada == 1:
        print("Você pode realizar o empréstimo! ")
    else:
        print("Opção inexistente!")
else:
    print("Opção inexistente!")