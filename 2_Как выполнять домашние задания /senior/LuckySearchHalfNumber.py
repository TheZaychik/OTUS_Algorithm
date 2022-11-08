from testingSystem import TestingSystem


def get_next_arr(perv_arr: list) -> list:
    new_len = len(perv_arr) + 9
    next_arr = []
    for i in range(new_len):
        q = 0
        for j in range(10):
            if 0 <= (i - j) < len(perv_arr):
                q += perv_arr[i - j]
        next_arr.append(q)
    return next_arr


def find_tickets_count(n: int) -> int:
    n *= 2
    arr = [1] * 10
    result = 0

    for i in range(n // 2 - 1):
        arr = get_next_arr(arr)
    for r in arr:
        result += r ** 2

    return result


if __name__ == '__main__':
    test = TestingSystem(r'../files/A01_Счастливые_билеты-1801-057a77/1.Tickets')
    test.run_test(find_tickets_count)
