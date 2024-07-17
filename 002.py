def Fibonacci():
    a, b = 1, 2

    while True:
        yield a
        a, b = b, a + b


# Inicializar variables para llevar la suma y el término actual
suma = 0
for num in Fibonacci():
    if num > 4000000:
        break
    if num % 2 == 0:  # Verificar si el número es par
        suma += num

print("La suma de los términos pares de la secuencia de Fibonacci hasta 4 millones es:", suma)
