from __future__ import annotations
from utils import arg_one_is_char

A = 128


class Node:
    def __init__(self) -> None:
        self.child = [None] * A
        self.isEnd = False

    @arg_one_is_char
    def exists(self, c: str) -> bool:
        return self.child[ord(c)] is not None

    @arg_one_is_char
    def next(self, c: str):
        if not self.exists(c):
            self.child[ord(c)] = Node()
        return self.child[ord(c)]


class Trie(object):

    def __init__(self, root: Node = Node()) -> None:
        self.root = root

    def insert(self, word: str) -> None:
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            node = node.next(c)
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        :type word: str
        :rtype: bool
        """
        node = self.go(word)
        if not node:
            return False
        return node.isEnd

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


if __name__ == '__main__':
    obj = Trie()
    obj.insert('word')
    print(obj.search('word'))
    print(obj.startsWith('wo'))
    print(obj.search('wo'))
    print(obj.startsWith('rd'))
