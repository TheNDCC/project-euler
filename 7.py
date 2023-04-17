def is_prime(n):
    if n == 0 or n == 4 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


primos = 0
num = 2

while True:
    if is_prime(num):
        primos += 1
    if primos == 10001:
        print(num)
        break
    num += 1
