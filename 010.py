import time

start_time = time.time()


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


sumar_primo = 2
for num in range(3, 2000000, 2):
    if is_prime(num):
        sumar_primo += num

print(sumar_primo)

end_time = time.time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos")
