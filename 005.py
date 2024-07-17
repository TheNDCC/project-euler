# Función para calcular el máximo común divisor (GCD) de dos números
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para calcular el mínimo común múltiplo (LCM) de dos números


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# Inicializamos el LCM con 1
lcm_result = 1

# Iteramos del 1 al 20 y actualizamos el LCM en cada iteración
for i in range(1, 21):
    lcm_result = lcm(lcm_result, i)

# El resultado final es el LCM de los números del 1 al 20
print("El número más pequeño divisible por los números del 1 al 20 es:", lcm_result)
