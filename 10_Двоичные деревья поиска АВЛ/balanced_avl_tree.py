from __future__ import annotations
from dataclasses import dataclass


@dataclass
class AVLNode:
    value: object
    height: int = 1
    left: AVLNode = None
    right: AVLNode = None


class AVLTree:

    def height(self, node: AVLNode) -> int:
        if node is None:
            return 0
        else:
            return node.height

    def balance(self, node: AVLNode) -> int:
        if node is None:
            return 0
        else:
            return self.height(node.left) - self.height(node.right)

    def minimum_value_node(self, node: AVLNode) -> AVLNode | None:
        if node is None or node.left is None:
            return node
        else:
            return self.minimum_value_node(node.left)

    def rotate_r(self, node: AVLNode) -> AVLNode:
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotate_l(self, node: AVLNode) -> AVLNode:
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def insert(self, val: object, root: AVLNode | None) -> AVLNode:
        if root is None:
            return AVLNode(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotate_r(root)
        if balance < -1 and val > root.right.value:
            return self.rotate_l(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotate_l(root.left)
            return self.rotate_r(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotate_l(root.right)
            return self.rotate_l(root)
        return root

    def preorder(self, root: AVLNode) -> None:
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def delete(self, val: object, node: AVLNode) -> AVLNode | None:
        if node is None:
            return node
        elif val < node.value:
            node.left = self.delete(val, node.left)
        elif val > node.value:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None:
                lt = node.right
                node = None
                return lt
            elif node.right is None:
                lt = node.left
                node = None
                return lt
            rgt = self.minimum_value_node(node.right)
            node.value = rgt.value
            node.right = self.delete(rgt.value, node.right)
        if node is None:
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance > 1 and self.balance(node.left) >= 0:
            return self.rotate_r(node)
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotate_l(node)
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotate_l(node.left)
            return self.rotate_r(node)
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.rotate_r(node.right)
            return self.rotate_l(node)
        return node


if __name__ == '__main__':
    tree = AVLTree()
    rt = None
    rt = tree.insert(3, rt)
    rt = tree.insert(5, rt)
    rt = tree.insert(7, rt)
    tree.preorder(rt)
