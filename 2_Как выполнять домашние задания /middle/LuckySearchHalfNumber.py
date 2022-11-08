from os import listdir
from os.path import isfile, join


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


def run_with_test() -> None:
    path = r'../files/A01_Счастливые_билеты-1801-057a77/1.Tickets'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files.sort()
    print(files)
    test_count, test_passed, test_failed = 0, 0, 0
    for in_f in files:
        if '.in' in in_f:
            print('-------------------------')
            out_f = in_f.replace('.in', '.out')
            test_count += 1
            try:
                with open(join(path, in_f), 'r') as f:
                    in_parameter = int(f.readline())
                with open(join(path, out_f), 'r') as f:
                    out_parameter = int(f.readline())
            except Exception as e:
                print('Ошибка при чтении файла:', str(e))
                test_failed += 1
                continue
            print(f'Тестовый входной файл: {in_f}, значение {in_parameter}')
            print(f'Тестовый выходной файл: {out_f}, значение {out_parameter}')
            out = find_tickets_count(in_parameter)
            print(f'Полученное значение {out}\nОжидаемое значние {out_parameter}')
            if out == out_parameter:
                print('Тест пройден')
                test_passed += 1
            else:
                print('Тест не пройден')
                test_failed += 1
    print('-------------------------')
    print(f'Итого:\nВсего тестов: {test_count}, пройдено: {test_passed}, завалено: {test_failed}')


if __name__ == '__main__':
    run_with_test()
