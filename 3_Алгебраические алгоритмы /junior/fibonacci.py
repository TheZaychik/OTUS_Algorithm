def iter_fibonacci(n: int) -> int:
    a, b, c = 1, 1, 0
    for _ in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return c


def recursive_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


if __name__ == '__main__':
    print('Итеративный алгоритм')
    print(iter_fibonacci(10))
    print(iter_fibonacci(15))
    print(iter_fibonacci(20))
    print('Рекурсивный алгоритм')
    print(recursive_fibonacci(10))
    print(recursive_fibonacci(15))
    print(recursive_fibonacci(20))
