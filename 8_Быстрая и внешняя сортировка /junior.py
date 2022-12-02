import random
import time
import sys

sys.setrecursionlimit(15000)


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

    def _swap(self, x: int, y: int) -> None:
        self.asg += 3
        tmp = self.mas[x]
        self.mas[x] = self.mas[y]
        self.mas[y] = tmp

    def _sort_quick(self, l: int, r: int) -> None:
        if l >= r:
            self.cmp += 1
            return
        m = self._split(l, r)
        self._sort_quick(l, m - 1)
        self._sort_quick(m + 1, r)

    def _split(self, l: int, r: int) -> int:
        p = self.mas[r]
        m = l - 1
        j = l
        while j <= r:
            if self.mas[j] <= p:
                self.cmp += 1
                m += 1
                self._swap(m, j)
            j += 1
        return m

    def quick_sort(self) -> None:
        self._sort_quick(0, self.n - 1)

    def _merge(self, l: int, x: int, r: int) -> None:
        M = [0] * (r - l + 1)
        a = l
        b = x + 1
        m = 0
        while (a <= x) and (b <= r):
            if self.mas[a] < self.mas[b]:
                M[m] = self.mas[a]
                m += 1
                a += 1
            else:
                M[m] = self.mas[b]
                m += 1
                b += 1
            self.cmp += 1
            self.asg += 1
        while a <= x:
            M[m] = self.mas[a]
            m += 1
            a += 1
            self.asg += 1
        while b <= r:
            M[m] = self.mas[b]
            m += 1
            b += 1
            self.asg += 1

        for i in range(l, r + 1):
            self.mas[i] = M[i - l]

    def _sort_merge(self, l: int, r: int) -> None:
        if l >= r:
            return
        m = (l + r) // 2
        self._sort_merge(l, m)
        self._sort_merge(m + 1, r)
        self._merge(l, m, r)

    def merge_sort(self) -> None:
        self._sort_merge(0, self.n - 1)


def test(n: int) -> None:
    def current_milliseconds() -> int:
        return round(time.time() * 1000)

    mas_a = [random.randint(0, 999) for _ in range(n)]

    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.quick_sort()
    # print(f'Quick N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')
    #
    srt = Sort(mas_a)
    start = current_milliseconds()
    srt.merge_sort()
    print(f'Merge N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')


if __name__ == '__main__':
    n = 100
    for _ in range(5):
        test(n)
        n *= 10
    # lst = [0, 5, 3, 2, 7, 89, 53, 123, 78764, 3457, 90]
    # srt = Sort(lst)
    # print(srt.mas)
    # srt.merge_sort()
    # print(srt.mas)
