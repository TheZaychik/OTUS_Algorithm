def sieve_ON(n: int) -> None:
    lp = [0] * (n + 2)
    pr = []
    for i in range(2, n):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)

        for p in pr:
            if p <= lp[i] and p * i <= n:
                lp[p * i] = p
            else:
                break
    print(f'{n} - {len(pr)}')


if __name__ == '__main__':
    print('Aлгоритм "Решето Эратосфена" O(N)')
    n = 10
    for _ in range(10):
        sieve_ON(n)
        n *= 10
