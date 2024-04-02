e1 = float(input("Digite a estatura da pessoa 1: "))
e2 = float(input("Digite a estatura da pessoa 2: "))
e3 = float(input("Digite a estatura da pessoa 3: "))

if e1 > e2 and e1 > e3:
    if e2 > e3:
        print(f"1 - {e1}\n2 - {e2}\n3 - {e3}")
    if e3 > e2:
        print(f"1 - {e1}\n2 - {e3}\n3 - {e2}")
elif e2 > e1 and e2 > e3:
    if e1 > e3:
        print(f"1 - {e2}\n2 - {e1}\n3 - {e3}")
    if e3 > e1:
        print(f"1 - {e2}\n2 - {e3}\n3 - {e1}")
elif e3 > e2 and e3 > e1:
    if e2 > e1:
        print(f"1 - {e3}\n2 - {e2}\n3 - {e1}")
    if e1 > e2:
        print(f"1 - {e3}\n2 - {e1}\n3 - {e2}")