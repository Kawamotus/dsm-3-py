import os
os.system('cls')

print("Calculadora de descontos :D")

precoTotal = float(input("Digite o valor total da compra em R$: "))
formaPagamento = int(input("Escolha a forma de pagamento: \n1 - À vista (em espécie)\n2 - Cartão de débito \n3 - Cartão de crédito (vencimento)\n"))

match formaPagamento:
    case 1:
        d = precoTotal * 0.85
        print(f"O valor da compra de R${precoTotal} passou a ser R${d}")
    case 2:
        d = precoTotal * 0.9
        print(f"O valor da compra de R${precoTotal} passou a ser R${d}")
    case 3:
        d = precoTotal * 0.95
        print(f"O valor da compra de R${precoTotal} passou a ser R${d}")
    case _:
        print("Opção inválida!")