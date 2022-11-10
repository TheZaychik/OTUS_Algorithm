def is_prime(n: int) -> bool:
    dividers_count = 0
    for divider in range(1, n + 1):
        if n % divider == 0:
            dividers_count += 1
    return dividers_count == 2


def get_primes_count(n: int) -> None:
    count = 0
    for i in range(n):
        if is_prime(i):
            count += 1
    print(f'{n} - {count}')


if __name__ == '__main__':
    primes_count = 0
    n = 10
    for _ in range(10):
        get_primes_count(n)
        n *= 10
