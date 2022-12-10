from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BSTNode:
    k: int
    v: object
    left: BSTNode = None
    right: BSTNode = None


class BinarySearchTree:

    def __init__(self, first_node: BSTNode) -> None:
        self.head = first_node

    def _insert(self, node: BSTNode, elem: BSTNode) -> BSTNode:
        if elem is None:
            return node
        if node.k < elem.k:
            elem.left = self._insert(node, elem.left)
        else:
            elem.right = self._insert(node, elem.right)
        return elem

    def insert(self, node: BSTNode) -> None:
        self._insert(node, self.head)

    def _search(self, key: int, elem: BSTNode) -> bool:
        if elem:
            if elem.k == key:
                return True
            elif elem.k < key:
                return self._search(key, elem.left)
            else:
                return self._search(key, elem.right)
        return False

    def search(self, key: int) -> bool:
        return self._search(key, self.head)

    @staticmethod
    def min_value_node(node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _remove(self, key: int, elem: BSTNode) -> BSTNode:
        if key < elem.k:
            elem.left = self._remove(key, elem.left)
        elif key > elem.k:
            elem.right = self._remove(key, elem.right)
        else:
            if elem.left is None:
                temp = elem.right
                return temp

            elif elem.right is None:
                temp = elem.left
                return temp

            temp = self.min_value_node(elem.right)
            elem.k = temp.k
            elem.right = self._remove(temp.k, elem.right)

        return elem

    def remove(self, key: int) -> None:
        self._remove(key, self.head)

    def _show_tree(self, elem: BSTNode = None) -> list:
        tree = [{elem.k: elem.v}]
        if elem.left:
            tree.append(self._show_tree(elem.left))
        if elem.right:
            tree.append(self._show_tree(elem.right))
        return tree

    def show_tree(self) -> list:
        return self._show_tree(self.head)


if __name__ == '__main__':
    bst = BinarySearchTree(BSTNode(40, 'data'))
    bst.insert(BSTNode(30, 'hello'))
    bst.insert(BSTNode(50, 'hi'))
    bst.insert(BSTNode(47, 'halo'))
    print(bst.search(40))
    bst.remove(50)
    print(bst.show_tree())

