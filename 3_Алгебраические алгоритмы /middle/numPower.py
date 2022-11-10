def multiplication_exp(a: int, n: int | float) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * multiplication_exp(a, n - 1)
    elif n % 2 == 0:
        return multiplication_exp(a * a, n / 2)


def binary_decomposition_exp(a: int, n: int) -> int:
    d = a
    p = 1
    i = n
    while i >= 1:
        i //= 2
        d = d * d
        if i % 2 == 1:
            p = p * d
    if n % 2 == 1:
        p *= a
    return p


if __name__ == '__main__':
    print('Алгоритм возведения в степень через домножение')
    print(multiplication_exp(2, 9))
    print(multiplication_exp(5, 2))
    print('Алгоритм возведения в степень через двоичное разложение показателя степени')
    print(binary_decomposition_exp(2, 9))
    print(binary_decomposition_exp(5, 2))
