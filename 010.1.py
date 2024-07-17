import time

start_time = time.time()


def sum_primes(n: int) -> int:
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, n, i):
                is_prime[j] = False
    return sum(i for i in range(n) if is_prime[i])


sumar_primo = sum_primes(2000000)
print(sumar_primo)

end_time = time.time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos")
