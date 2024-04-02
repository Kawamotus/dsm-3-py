b = int(input("Digite o número de votos brancos: "))
n = int(input("Digite o número de votos nulos: "))
v = int(input("Digite o número de votos válidos: "))

t  = b + n + v

pb = (b*100)/t
pn = (n*100)/t
pv = (v*100)/t

print(f"Segue o percentual de votos: \nBrancos: {pb:.2f}\nNulos: {pn:.2f}\nVálidos: {pv:.2f}\n\nTotal de eleitores: {t}")