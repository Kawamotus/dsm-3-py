import os
os.system('cls')

#contagem de 1 a 100
for i in range (1, 101): #sempre coloca um número a mais, no caso vai até 100, do 1 ao 100
    print(i)

qtd = 0


#soma de 1 a 100
for i in range(1, 101):
    qtd += i

print(f"A soma total de 1 a 100 é {qtd}")

#repetição de 1 a 100 de 2 em 2
for i in range(1, 101, 2):  #o 2 no final é de quanto em quanto
    print(i)