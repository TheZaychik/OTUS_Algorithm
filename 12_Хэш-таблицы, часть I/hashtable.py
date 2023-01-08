from time import time


class Node:
    def __init__(self, key: str, value: object = None) -> None:
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int) -> None:
        self.data = [None] * size
        self.size = size

    @staticmethod
    def hash_function(key: str, size: int) -> int:
        hash_key = ''
        for k in key:
            hash_key += str(ord(k))

        return int(hash_key) % size

    def add(self, key: str, value: object) -> None:
        hash_value = self.hash_function(key, self.size)
        if self.data[hash_value] is None:
            self.data[hash_value] = Node(key, value)
        else:
            temp = Node(key)
            p = self.data[hash_value]
            while p.next is not None:
                p = p.next
            p.next = temp

    def get(self, key: str) -> object:
        hash_value = self.hash_function(key, self.size)
        if self.data[hash_value] is not None and self.data[hash_value].key == key:
            return self.data[hash_value].value
        else:
            p = self.data[hash_value]
            while p is not None and p.key != key:
                p = p.next
            if p is not None and p.key == key:
                return p.value
        return False

    def delete(self, key: str) -> None | str:
        if not self.get(key):
            return 'Нет такого объекта'
        hash_value = self.hash_function(key, self.size)

        if self.data[hash_value] is not None and self.data[hash_value].key == key:
            self.data[hash_value] = None
        else:
            p = self.data[hash_value]
            pre = None
            while p is not None and p.data != key:
                pre = p
                p = p.next
            if p is None:
                return 'Delete Error'
            else:
                pre.next = p.next


def get_random_word() -> str:
    import random
    import string

    letters = string.ascii_letters
    x = "".join(random.sample(letters, 5))
    return x


def time_test() -> None:
    start = time()
    ht = HashTable(10)
    for i in range(10000):
        word = get_random_word()
        ht.add(word, i)
        ht.get(word)
        ht.delete(word)

    print(time() - start)


if __name__ == '__main__':
    # ht = HashTable(10)
    # ht.add('odin', 1)
    # print(ht.get('odin'))
    # ht.add('dva', 2)
    # print(ht.get('dva'))
    # ht.delete('dva')
    # print(ht.get('dva'))
    time_test()
