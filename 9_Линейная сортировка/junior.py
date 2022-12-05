import sys
import random
import time


class Sort:

    @staticmethod
    def find_max(mas: list[int]) -> int:
        max_el = -sys.maxsize - 1
        for i in mas:
            if i > max_el:
                max_el = i
        return max_el

    @staticmethod
    def bucket_sort(mas: list[int]) -> list[int]:
        sorted_mas = []
        mas_len = len(mas)
        bucket = [0] * mas_len
        for i in range(mas_len):
            bucket[i] = []
        max_el = Sort.find_max(mas)

        for i in range(mas_len):
            index = mas[i] * mas_len // (max_el + 1)
            bucket_len = len(bucket[index])
            if bucket_len == 0:
                bucket[index].append(mas[i])
                continue

            for j in range(bucket_len):
                if bucket[index][j] >= mas[i]:
                    bucket[index].insert(j, mas[i])
                    break
                elif bucket[index][j] < mas[i] and j + 1 == bucket_len:
                    bucket[index].insert(j + 1, mas[i])
                    break

        for i in range(len(bucket)):
            for j in range(len(bucket[i])):
                sorted_mas.append(bucket[i][j])

        return sorted_mas

    @staticmethod
    def counting_sort(mas: list[int]) -> list[int]:
        max_el = Sort.find_max(mas)
        sorted_mas = [0] * len(mas)
        indexes = [0] * (max_el + 1)
        for el in mas:
            indexes[el] += 1
        for i in range(1, len(indexes)):
            indexes[i] += indexes[i - 1]

        for i in range(len(mas) - 1, -1, -1):
            indexes[mas[i]] -= 1
            sorted_mas[indexes[mas[i]]] = mas[i]

        return sorted_mas

    @staticmethod
    def radix_sort(mas: list[int]) -> list[int]:
        max_el = Sort.find_max(mas)
        digits = 0
        while (max_el // (10 ** digits)) % 10 != 0:
            sorted_mas = [0] * len(mas)
            indexes = [0] * 10
            for m in mas:
                el = (m // (10 ** digits)) % 10
                indexes[el] += 1
            for i in range(1, len(indexes)):
                indexes[i] += indexes[i - 1]
            for i in range(len(mas) - 1, -1, -1):
                el = (mas[i] // (10 ** digits)) % 10
                indexes[el] -= 1
                sorted_mas[indexes[el]] = mas[i]
            mas = sorted_mas
            digits += 1
        return mas


def test(n: int) -> None:
    def current_milliseconds() -> int:
        return round(time.time() * 1000)

    mas_a = [random.randint(0, 999) for _ in range(n)]

    # start = current_milliseconds()
    # Sort.bucket_sort(mas_a)
    # print(f'Bucket N: {n} time: {current_milliseconds() - start}')

    # start = current_milliseconds()
    # Sort.counting_sort(mas_a)
    # print(f'Counting N: {n} time: {current_milliseconds() - start}')

    start = current_milliseconds()
    Sort.radix_sort(mas_a)
    print(f'Radix N: {n} time: {current_milliseconds() - start}')


if __name__ == '__main__':
    n = 100
    for _ in range(5):
        test(n)
        n *= 10
