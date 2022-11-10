import math


def is_prime(n: int, primes: [int]) -> bool:
    sqrt = int(math.sqrt(n))
    i = 0
    while primes[i] <= sqrt:
        if n % primes[i] == 0:
            return False
        i += 1
    return True


def get_primes_count(n: int) -> None:
    count = 0
    primes = [0] * (n // 2)
    primes[count] = 2
    count += 1
    for i in range(3, n + 1):
        if is_prime(i, primes):
            primes[count] = i
            count += 1
    print(f'{n} - {count}')


if __name__ == '__main__':
    print('Алгоритм поиска простых чисел с оптимизациями поиска и делением только на простые числа')
    primes_count = 0
    n = 10
    for _ in range(10):
        get_primes_count(n)
        n *= 10
