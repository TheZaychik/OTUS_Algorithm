def count(n: int) -> int:
    num = 0

    def recursive_count(recursive_n: int, sum_a=0, sum_b=0) -> None:
        nonlocal num
        if recursive_n == 0:
            if sum_a == sum_b:
                num += 1
            return

        for a in range(0, 10):
            for b in range(0, 10):
                recursive_count(recursive_n - 1, sum_a + a, sum_b + b)

    recursive_count(n)
    return num


if __name__ == '__main__':
    print(count(3))
    print(count(2))
    print(count(1))
