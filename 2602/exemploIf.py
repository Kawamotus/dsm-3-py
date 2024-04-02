import os
os.system('cls')

nome = input("Digite o nome do Aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media > 6:
    print(f"O Aluno {nome} está aprovado, média: {media:.2f}")
elif media >= 2 and media <= 6:
    print(f"O Aluno está de exame")
else:
    print(f"O Aluno {nome} está reprovado, média: {media:.2f}")