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

    def bubble_plus(self) -> None:
        for j in range(self.n - 1, -1, -1):
            for i in range(self.n - j - 1):
                if self.mas[i] > self.mas[i + 1]:
                    self.cmp += 1
                    self._swap(i, i + 1)

    def _swap(self, x: int, y: int) -> None:
        self.asg += 3
        tmp = self.mas[x]
        self.mas[x] = self.mas[y]
        self.mas[y] = tmp

    def insertion_shift(self) -> None:
        i = 0
        for j in range(1, self.n):
            k = self.mas[j]
            self.asg += 1
            i = j - 1
            while i >= 0 and self.mas[i] > k:
                self.cmp += 1
                self.mas[i + 1] = self.mas[i]
                self.asg += 1
                i -= 1
            self.mas[i + 1] = k
            self.asg += 1

    def insertion_binary(self) -> None:
        i = 0
        for j in range(1, self.n):
            k = self.mas[j]
            self.asg += 1
            p = self._binary_search(k, 0, j - 1)
            i = j - 1
            while i >= p and self.mas[i] > k:
                self.mas[i + 1] = self.mas[i]
                self.asg += 1
                i -= 1
            self.mas[i + 1] = k
            self.asg += 1

    def _binary_search(self, key: int, low: int, high: int) -> int:
        if high <= low:
            if key > self.mas[low]:
                return low + 1
            else:
                return low
        self.cmp += 1
        mid = (low + high) // 2
        if key > self.mas[mid]:
            return self._binary_search(key, mid + 1, high)
        else:
            return self._binary_search(key, low, mid - 1)

    def shell_sort_4(self) -> None:
        gap = self.n // 4
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

    def shell_sort_8(self) -> None:
        gap = self.n // 8
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
    # srt.bubble_plus()
    # print(f'Bubble+ N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')

    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.insertion_shift()
    # print(f'InsertionShift N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')
    #
    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.insertion_binary()
    # print(f'InsertionBinary N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')

    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.shell_sort_4()
    # print(f'Shell4 N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')
    #
    srt = Sort(mas_a)
    start = current_milliseconds()
    srt.shell_sort_8()
    print(f'Shell8 N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')


if __name__ == '__main__':
    n = 100
    for _ in range(5):
        test(n)
        n *= 10
