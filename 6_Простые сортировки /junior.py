import random
import time


class Sort:
    mas: list[int]
    n: int
    cmp: int
    asg: int

    def __init__(self, mas: list):
        self.mas = mas
        self.n = len(mas)
        self.cmp = 0
        self.asg = 0

    def bubble_sort(self) -> None:
        for j in range(self.n - 1, -1, -1):
            for i in range(j):
                if self.mas[i] > self.mas[i + 1]:
                    self.cmp += 1
                    self._swap(i, i + 1)

    def _swap(self, x: int, y: int) -> None:
        self.asg += 3
        tmp = self.mas[x]
        self.mas[x] = self.mas[y]
        self.mas[y] = tmp

    def insertion_sort(self) -> None:
        for j in range(1, self.n):
            for i in range(j - 1, -1, -1):
                if self.mas[i] > self.mas[i + 1]:
                    self.cmp += 1
                    self._swap(i, i + 1)

    def shell_sort(self) -> None:
        gap = self.n // 2
        while gap > 0:
            i = gap
            while i < self.n:
                j = i
                while j > gap and self.mas[j - gap] > self.mas[j]:
                    self.cmp += 1
                    self._swap(j - gap, j)
                    j -= gap
                i += 1
            gap //= 2


def current_milliseconds() -> int:
    return round(time.time() * 1000)


def test(n: int) -> None:
    mas_a = [random.randint(0, 999) for _ in range(n)]

    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.bubble_sort()
    # print(f'Bubble N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')

    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.insertion_sort()
    # print(f'Insertion N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')

    srt = Sort(mas_a)
    start = current_milliseconds()
    srt.shell_sort()
    print(f'Shell N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')


if __name__ == '__main__':
    n = 100
    for _ in range(5):
        test(n)
        n *= 10
