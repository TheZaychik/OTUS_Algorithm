from __future__ import annotations
from time import time
from dataclasses import dataclass


@dataclass
class SplayNode:
    key: int
    left: SplayNode = None
    parent: SplayNode = None
    right: SplayNode = None


class SplayTree:

    @staticmethod
    def set_parent(child: SplayNode, parent: SplayNode | None) -> None:
        if child is not None:
            child.parent = parent

    @staticmethod
    def keep_parent(v: SplayNode) -> None:
        SplayTree.set_parent(v.left, v)
        SplayTree.set_parent(v.right, v)

    @staticmethod
    def rotate(parent: SplayNode, child: SplayNode) -> None:
        gparent = parent.parent
        if gparent is not None:
            if gparent.left == parent:
                gparent.left = child
            else:
                gparent.right = child
        if parent.left == child:
            parent.left, child.right = child.right, parent
        else:
            parent.right, child.left = child.left, parent
        SplayTree.keep_parent(child)
        SplayTree.keep_parent(parent)
        child.parent = gparent

    @staticmethod
    def splay(v: SplayNode) -> SplayNode:
        if v.parent is None:
            return v
        parent = v.parent
        gparent = parent.parent
        if gparent is None:
            SplayTree.rotate(parent, v)
            return v
        else:
            zigzig = (gparent.left == parent) == (parent.left == v)
            if zigzig:
                SplayTree.rotate(gparent, parent)
                SplayTree.rotate(parent, v)
            else:
                SplayTree.rotate(parent, v)
                SplayTree.rotate(gparent, v)
            return SplayTree.splay(v)

    @staticmethod
    def find(v: SplayNode, key: int) -> object:
        if v is None:
            return None
        if key == v.key:
            return SplayTree.splay(v)
        if key < v.key and v.left is not None:
            return SplayTree.find(v.left, key)
        if key > v.key and v.right is not None:
            return SplayTree.find(v.right, key)
        return SplayTree.splay(v)

    @staticmethod
    def split(root: SplayNode, key: int) -> (SplayNode, SplayNode):
        if root is None:
            return None, None
        root = SplayTree.find(root, key)
        if root.key == key:
            SplayTree.set_parent(root.left, None)
            SplayTree.set_parent(root.right, None)
            return root.left, root.right
        if root.key < key:
            right, root.right = root.right, None
            SplayTree.set_parent(right, None)
            return root, right
        else:
            left, root.left = root.left, None
            SplayTree.set_parent(left, None)
            return left, root

    @staticmethod
    def insert(root: SplayNode, key: int):
        left, right = SplayTree.split(root, key)
        root = SplayNode(key=key, left=left, right=right)
        SplayTree.keep_parent(root)
        return root

    @staticmethod
    def merge(left: SplayNode | None, right: SplayNode | None):
        if right is None:
            return left
        if left is None:
            return right
        right = SplayTree.find(right, left.key)
        right.left, left.parent = left, right
        return right

    @staticmethod
    def remove(root: SplayNode, key: int):
        root = SplayTree.find(root, key)
        SplayTree.set_parent(root.left, None)
        SplayTree.set_parent(root.right, None)
        return SplayTree.merge(root.left, root.right)


if __name__ == '__main__':
    start = time()
    root = SplayTree.insert(SplayNode(50), 50)
    root = SplayTree.insert(root, 47)
    root = SplayTree.insert(root, 25)
    root = SplayTree.insert(root, 21)
    root = SplayTree.remove(root, 47)
    print(time() - start)
