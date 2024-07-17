from typing import List


class PrimeGenerator:
    def __init__(self):
        # Inicializa la lista de primos con el primer primo, que es 2
        self.primes = [2]

    def generate_primes(self, n: int) -> List[int]:
        """Genera n números primos y los devuelve en una lista."""
        while len(self.primes) < n:
            # Comienza a buscar primos a partir del último primo en la lista
            num = self.primes[-1] + 1
            while True:
                for prime in self.primes:
                    if num % prime == 0:
                        break
                else:
                    self.primes.append(num)
                    break
                num += 1
        return self.primes[:n]


if __name__ == '__main__':
    prime_generator = PrimeGenerator()
    n = 10001  # Número de primos que se desea generar
    primes = prime_generator.generate_primes(n)
    print(f"El {n}º número primo es: {primes[-1]}")
