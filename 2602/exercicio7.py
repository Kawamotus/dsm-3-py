rg = input("Insira o RG do empregado: ")
anoNasc = int(input("Insira o ano do nascimento do empregado: "))
anoIngresso = int(input("Insira o ano de ingresso na empresa: "))
anoAtual = int(input("Insira o ano atual: "))

idade = anoAtual - anoNasc
tempoTrabalho = anoAtual - anoIngresso

if idade >= 65:
    print("Requerer aposentadoria")
elif tempoTrabalho >= 30:
    print("Requerer aposentadoria")
elif idade>= 60 and tempoTrabalho >=25:
    print("Requerer aposentadoria")
else:
    print("Não requerer aposentadoria")