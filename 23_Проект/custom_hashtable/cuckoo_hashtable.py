from typing import Any


class Node:
    def __init__(self, k: Any, d: Any) -> None:
        self.key = k
        self.data = d

    def __str__(self) -> str:
        return '(' + str(self.key) + ' : ' + str(self.data) + ')'


class CuckooHashTable:
    def __init__(self, size: int) -> None:
        self._hash_array1 = [None] * (size // 2)
        self._hash_array2 = [None] * (size // 2)
        self._node_count = 0
        self._size = size
        self._cycle = 0

    def __len__(self) -> int:
        return self._size

    def _hash_func(self, s: str) -> (int, int):
        x = hash(s)
        hash_key = ''
        for k in s:
            hash_key += str(ord(k))
        y = int(hash_key)

        size = self._size // 2

        return x % size, y % size

    def insert(self, k: Any, d: Any) -> bool:
        if self.find(k) is not None:
            return False
        n = Node(k, d)
        if self._node_count >= (self._size // 3):
            self._increase_tables()

        position1, position2 = self._hash_func(n.key)
        pos = position1
        table = self._hash_array1
        for i in range(5):  # 5 is max loop
            if table[pos] is None:
                table[pos] = n
                self._node_count += 1
                self._cycle = 0
                return True

            n, table[pos] = table[pos], n
            if pos == position1:
                position1, position2 = self._hash_func(n.key)
                pos = position2
                table = self._hash_array2
            else:
                position1, position2 = self._hash_func(n.key)
                pos = position1
                table = self._hash_array1

        self._cycle += 1
        if self._cycle >= 3:
            self._cycle = 0
            return False
        self._increase_tables()
        return self.insert(n.key, n.data)

    def __str__(self) -> str:
        return f'Хэш-массив 1: {[str(node) for node in self._hash_array1]}\n' \
               + f'Хэш-массив 2: {[str(node) for node in self._hash_array2]}'

    def _rehash(self, size: int) -> None:
        temp = CuckooHashTable(size)
        for i in range(self._size // 2):
            x = self._hash_array1[i]
            y = self._hash_array2[i]
            if x is not None:
                temp.insert(x.key, x.data)
            if y is not None:
                temp.insert(y.key, y.data)

        self._hash_array1 = temp._hash_array1
        self._hash_array2 = temp._hash_array2
        self._node_count = temp._node_count
        self._size = temp._size
        self._cycle = 0

    def _increase_tables(self) -> None:
        new_size = self._size * 2
        self._rehash(new_size)

    def find(self, k: Any) -> Any:
        pos1, pos2 = self._hash_func(k)
        x = self._hash_array1[pos1]
        y = self._hash_array2[pos2]
        if x is not None and x.key == k:
            return x.data
        if y is not None and y.key == k:
            return y.data

        return None

    def delete(self, k: Any) -> bool:
        pos1, pos2 = self._hash_func(k)
        x = self._hash_array1[pos1]
        y = self._hash_array2[pos2]
        if x is not None and x.key == k:
            self._hash_array1[pos1] = None
        elif y is not None and y.key == k:
            self._hash_array2[pos2] = None
        else:
            return False
        self._node_count -= 1
        return True
