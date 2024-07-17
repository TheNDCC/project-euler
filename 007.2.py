def is_prime(n: int) -> bool:
    """
    Verifica si un número es primo.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_nth_prime(n: int) -> int:
    """
    Obtiene el n-ésimo número primo.
    """
    primos = 0
    num = 2

    while True:
        if is_prime(num):
            primos += 1
            if primos == n:
                return num
        num += 1


n = 10001  # Valor de n para el que se desea encontrar el n-ésimo número primo
result = get_nth_prime(n)
print(f"El {n}-ésimo número primo es: {result}")
