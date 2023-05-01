a = 0
b = 0
c = 0
ciclo = 0

for m in range(1, 1000):
    for n in range(1, m):
        ciclo += 1
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a+b+c == 1000 and a**2 + b**2 == c**2:
            resultado = a*b*c
            break
    else:
        continue
    break
print(f"{a} x {b} x {c} = {resultado}")
print(ciclo)
