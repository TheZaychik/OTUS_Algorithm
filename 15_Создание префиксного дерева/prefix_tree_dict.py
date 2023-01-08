from __future__ import annotations
from typing import Any
from utils import arg_one_is_char
from time import time

A = 128


class Node:
    def __init__(self, value: Any = None) -> None:
        self.child = [None] * A
        self.value = value
        self.isEnd = False

    @arg_one_is_char
    def exists(self, c: str) -> bool:
        return self.child[ord(c)] is not None

    @arg_one_is_char
    def next(self, c: str):
        if not self.exists(c):
            self.child[ord(c)] = Node()
        return self.child[ord(c)]

    def child_count(self) -> int:
        count = 0
        for c in self.child:
            if c:
                count += 1
        return count


class TrieDict(object):

    def __init__(self, root: Node = Node()) -> None:
        self.root = root

    def insert(self, word: str, value: Any) -> None:
        """
        :type word: str
        :type value: Any
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.next(c)
        node.value = value
        node.isEnd = True

    def _remove(self, postfix: str, node: Node) -> bool:
        if len(postfix) == 1:
            if node.isEnd:
                return True
            else:
                node.value = None
                return False

        if self._remove(postfix[1:], node.next(postfix[:1])):
            node.child[ord(postfix[:1])] = None
            if node.child_count() >= 1:
                return False
            if node.value is not None:
                node.isEnd = True
                return False
            return True

        return False

    def remove(self, word: str) -> None:
        """
        :type word: str
        :rtype: bool
        """
        self._remove(word, self.root)

    def search(self, word: str) -> Any:
        """
        :type word: str
        :rtype: Any
        """
        node = self.go(word)
        if not node:
            return False
        return node.value

    def go(self, word: str) -> Node | None:
        node = self.root
        for c in word:
            if node.exists(c):
                node = node.next(c)
            else:
                return None
        return node

    def startsWith(self, prefix: str) -> bool:
        """
        :type prefix: str
        :rtype: bool
        """
        return self.go(prefix) is not None


def get_random_word() -> str:
    import random
    import string

    letters = string.ascii_letters
    x = "".join(random.sample(letters, 5))
    return x


def time_test() -> None:
    start = time()
    obj = TrieDict()
    for i in range(10000):
        word = get_random_word()
        obj.insert(word, i)
        obj.search(word)
        obj.remove(word)
    print(time() - start)


if __name__ == '__main__':
    # obj = TrieDict()
    # obj.insert('word', 'hello')
    # print(obj.search('word'))
    # print(obj.search('wordword'))
    # print(obj.remove('word'))
    # print(obj.search('word'))
    # obj.insert('word', 'hell2')
    # print(obj.search('word'))
    time_test()
