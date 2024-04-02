salarioMensal = float(input("Digite o valor do salário do funcionário: "))
percentualReajuste = float(input("Digite o percentual de reajuste (0 - 100): "))

novoSalario = salarioMensal + (salarioMensal * percentualReajuste)/100

print(f"O novo salário é de: {novoSalario}")