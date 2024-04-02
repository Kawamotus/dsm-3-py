d = input("Digite a descrição do produto (nome): ")
qtd = int(input("Digite a quantidade comprada do produto: "))
p = float(input("Digite o valor unitário do produto: "))

pf = qtd * p

print(f"O valor total da compra de {d} é {pf}({qtd}x{p})")