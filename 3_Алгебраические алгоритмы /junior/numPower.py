def iter_num_power(a: int, n: int) -> int:
    num_pwr = a
    for _ in range(1, n):
        num_pwr *= a
    return num_pwr


if __name__ == '__main__':
    print(iter_num_power(2, 8))
    print(iter_num_power(5, 2))
