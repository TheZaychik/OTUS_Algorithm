import random


class Sort:

    @staticmethod
    def _swap(mas: list[int], x: int, y: int) -> None:
        tmp = mas[x]
        mas[x] = mas[y]
        mas[y] = tmp

    @staticmethod
    def _sort_quick(mas: list[int], l: int, r: int) -> None:
        if l >= r:
            return
        m = Sort._split(mas, l, r)
        Sort._sort_quick(mas, l, m - 1)
        Sort._sort_quick(mas, m + 1, r)

    @staticmethod
    def _split(mas: list[int], l: int, r: int) -> int:
        p = mas[r]
        m = l - 1
        j = l
        while j <= r:
            if mas[j] <= p:
                m += 1
                Sort._swap(mas, m, j)
            j += 1
        return m

    @staticmethod
    def quick_sort(mas: list[int]) -> None:
        Sort._sort_quick(mas, 0, len(mas) - 1)


def gen_file(n: int, t: int) -> None:
    with open('example.txt', 'w') as f:
        for _ in range(n):
            f.write(f'{random.randint(1, t)}\n')


def es1(t: int):
    pass


def es2():
    file = 1
    out = 0
    with open('example.txt', 'r') as exf:
        active = True
        while active:
            mas = []
            for _ in range(5):
                chunk = exf.readline().replace('\n', '')
                if chunk == '':
                    active = False
                else:
                    mas.append(int(chunk))
            Sort.quick_sort(mas)
            with open(f'file{file}.txt', 'a') as f:
                for i in mas:
                    f.write(f'{i}\n')
            file += 1 if file < 2 else -1
    # out1 = open(f'out{out}.txt', 'w'):
    #     active = True
    #     while active:


if __name__ == '__main__':
    gen_file(20, 40)
    es2()
    # mas = [5, 3, 6, 8, 2, 45, 68, 3]
    # Sort.quick_sort(mas)
    # print(mas)
