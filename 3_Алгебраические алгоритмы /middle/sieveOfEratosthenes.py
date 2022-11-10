def sieve_OLogN(n: int) -> None:
    count = 0
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j += i
        i += 1
    for i in a:
        if i != 0:
            count += 1
    print(f'{n} - {count}')


if __name__ == '__main__':
    print('Aлгоритм "Решето Эратосфена" O(N Log Log N)')
    n = 10
    for _ in range(10):
        sieve_OLogN(n)
        n *= 10
