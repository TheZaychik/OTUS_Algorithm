from __future__ import annotations
from time import time
from random import randint
from dataclasses import dataclass


@dataclass
class RandomNode:
    key: int
    size: int = 1
    left: RandomNode = None
    right: RandomNode = None


class RandomTree:
    @staticmethod
    def find(p: RandomNode, k: int):
        if not p:
            return None
        if k == p.key:
            return p
        if k < p.key:
            return RandomTree.find(p.left, k)
        else:
            return RandomTree.find(p.right, k)

    @staticmethod
    def insert(p: RandomNode, k: int):
        if not p:
            return RandomNode(k)
        if randint(0, 32767) % (p.size + 1) == 0:
            return RandomTree.insert_root(p, k)
        if p.key > k:
            p.left = RandomTree.insert(p.left, k)
        else:
            p.right = RandomTree.insert(p.right, k)
        RandomTree.fix_size(p)
        return p

    @staticmethod
    def min_value_node(node: RandomNode):
        current = node
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def remove(p: RandomNode, k: int):
        if not p:
            return p
        if p.key == k:
            if p.left is None:
                temp = p.right
                return temp
            elif p.right is None:
                temp = p.left
                return temp
            temp = RandomTree.min_value_node(p.right)
            p.key = temp.key
            p.right = RandomTree.remove(p.right, temp.key)
        elif k < p.key:
            p.left = RandomTree.remove(p.left, k)
        else:
            p.right = RandomTree.remove(p.right, k)
        return p

    @staticmethod
    def get_size(p: RandomNode):
        if not p:
            return 0
        return p.size

    @staticmethod
    def fix_size(p: RandomNode):
        p.size = RandomTree.get_size(p.left) + RandomTree.get_size(p.right) + 1

    @staticmethod
    def rotate_right(p: RandomNode):
        q = p.left
        if not q:
            return p
        p.left = q.right
        q.right = p
        q.size = p.size
        RandomTree.fix_size(p)
        return q

    @staticmethod
    def rotate_left(p: RandomNode):
        q = p.right
        if not q:
            return p
        p.right = q.left
        q.left = q
        p.size = q.size
        RandomTree.fix_size(q)
        return p

    @staticmethod
    def insert_root(p: RandomNode, k: int):
        if not p:
            return RandomNode(k)
        if k < p.key:
            p.left = RandomTree.insert_root(p.left, k)
            return RandomTree.rotate_right(p)
        else:
            p.right = RandomTree.insert_root(p.right, k)
            return RandomTree.rotate_left(p)


if __name__ == '__main__':
    start = time()
    root = RandomTree.insert(RandomNode(50), 50)
    root = RandomTree.insert(root, 47)
    root = RandomTree.insert(root, 25)
    root = RandomTree.insert(root, 21)
    root = RandomTree.remove(root, 47)
    print(time() - start)

