ap = float(input("Digite a altura da parede: "))
lp = float(input("Digite a largura da parede: "))
aa = float(input("Digite a altura do azulejo: "))
la = float(input("Digite a largura do azulejo: "))

areaParede = ap*lp
areaAzulejo = aa*la

totalAzulejo = areaParede/areaAzulejo

print(f"A quantidade necessária de azulejos é de: {totalAzulejo}")