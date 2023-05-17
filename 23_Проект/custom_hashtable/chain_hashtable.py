class Node:
    def __init__(self, key: str, data: object = None) -> None:
        self.key = key
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return "(" + str(self.key) + " : " + str(self.data) + ")"


class ChainHashTable:
    def __init__(self, size: int) -> None:
        self._hash_array = [None] * size
        self._size = size

    @staticmethod
    def _hash_func(key: str, _size: int) -> int:
        hash_key = ''
        for k in key:
            hash_key += str(ord(k))

        return int(hash_key) % _size

    def insert(self, key: str, data: object) -> None:
        hash_value = self._hash_func(key, self._size)
        if self._hash_array[hash_value] is None:
            self._hash_array[hash_value] = Node(key, data)
        else:
            temp = Node(key)
            p = self._hash_array[hash_value]
            while p.next is not None:
                p = p.next
            p.next = temp

    def find(self, key: str) -> object:
        hash_value = self._hash_func(key, self._size)
        if self._hash_array[hash_value] is not None and self._hash_array[hash_value].key == key:
            return self._hash_array[hash_value].data
        else:
            p = self._hash_array[hash_value]
            while p is not None and p.key != key:
                p = p.next
            if p is not None and p.key == key:
                return p.data
        return False

    def delete(self, key: str) -> None | str:
        if not self.get(key):
            return 'Нет такого объекта'
        hash_value = self._hash_func(key, self._size)

        if self._hash_array[hash_value] is not None and self._hash_array[hash_value].key == key:
            self._hash_array[hash_value] = None
        else:
            p = self._hash_array[hash_value]
            pre = None
            while p is not None and p.data != key:
                pre = p
                p = p.next
            if p is None:
                return 'Delete Error'
            else:
                pre.next = p.next
                
    def __str__(self) -> str:
        return f'Хэш-массив: {[str(node) for node in self._hash_array]}\n'
