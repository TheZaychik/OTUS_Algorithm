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

    def _swap(self, x: int, y: int) -> None:
        self.asg += 3
        tmp = self.mas[x]
        self.mas[x] = self.mas[y]
        self.mas[y] = tmp

    def _find_max(self, j: int) -> int:
        max_index = 0
        for i in range(1, j + 1):
            self.cmp += 1
            if self.mas[i] > self.mas[max_index]:
                max_index = i
        return max_index

    def _max_index(self, *args: [int]) -> int:
        max_index = args[0]
        for i in range(1, len(args)):
            if self.mas[args[i]] > self.mas[max_index]:
                max_index = args[i]
        return max_index

    def select_sort(self) -> None:
        for j in range(self.n - 1, 0, -1):
            self._swap(self._find_max(j), j)

    def _heapify(self, root: int, size: int) -> None:
        x = root
        l = 2 * x + 1
        r = l + 1
        self.cmp += 3
        if l < size and self.mas[l] > self.mas[x]:
            x = l
        if r < size and self.mas[r] > self.mas[x]:
            x = r
        if x == root:
            return
        self._swap(root, x)
        self._heapify(x, size)

    def heap_sort(self) -> None:
        for h in range(self.n // 2 - 1, -1, -1):
            self._heapify(h, self.n)
        for j in range(self.n - 1, 0, -1):
            self._swap(0, j)
            self._heapify(0, j)


def current_milliseconds() -> int:
    return round(time.time() * 1000)


def test(n: int) -> None:
    mas_a = [random.randint(0, 999) for _ in range(n)]

    srt = Sort(mas_a)
    start = current_milliseconds()
    srt.heap_sort()
    print(f'Heap N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')

    # srt = Sort(mas_a)
    # start = current_milliseconds()
    # srt.select_sort()
    # print(f'Select N: {n} cmp: {srt.cmp} asg: {srt.asg} time: {current_milliseconds() - start}')


if __name__ == '__main__':
    from testingSystem import TestingSystemMk2
    # test = TestingSystemMk2('/Users/nikitazaytsev/git/OTUS_Algorithm/7_Пирамидальная сортировка/files/0.random')
    # test = TestingSystemMk2('/Users/nikitazaytsev/git/OTUS_Algorithm/7_Пирамидальная сортировка/files/1.digits')
    # test = TestingSystemMk2('/Users/nikitazaytsev/git/OTUS_Algorithm/7_Пирамидальная сортировка/files/2.sorted')
    test = TestingSystemMk2('/Users/nikitazaytsev/git/OTUS_Algorithm/7_Пирамидальная сортировка/files/3.revers')
    test.run_test(Sort, 'select_sort')

