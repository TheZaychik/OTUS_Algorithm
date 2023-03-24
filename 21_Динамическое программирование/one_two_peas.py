def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return x % 2 != 0


def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if is_even(a) and is_even(b):
        return gcd(a >> 1, b >> 1) << 1

    if is_even(a) and is_odd(b):
        return gcd(a >> 1, b)
    if is_odd(a) and is_even(b):
        return gcd(a, b >> 1)
    if a > b:
        return gcd((a - b) >> 1, b)

    return gcd(a, (b - a) >> 1)


if __name__ == '__main__':
    print(gcd(100, 2))
