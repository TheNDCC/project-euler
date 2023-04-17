def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero


def capicua(numero):
    return numero == invertir_numero(numero)


mayor = 0
for i in range(100, 1000):
    print("Iterar i")
    for j in range(100, 1000):
        print(i, j)
        valor = i * j
        if capicua(valor):
            if valor > mayor:
                mayor = valor
                # print(i, j, valor)
print(mayor)
