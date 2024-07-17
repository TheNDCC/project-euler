def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime_factor(number: int) -> int:
    largest_factor = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            if is_prime(i):
                largest_factor = i
            if is_prime(number // i):
                largest_factor = max(largest_factor, number // i)
    return largest_factor


number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", result)
