from .avl_node import AVLNode
from ..LinkedList.LinkedList import LinkedList

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = AVLNode(key)
        else:
            self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key.model < node.key.model:
            node.left = self._insert(node.left, key)
        # ----------------------------------------------
        elif key.model == node.key.model:
            node.key.append(key.root.value)
        # ----------------------------------------------
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance_factor = self._get_balance(node)

        if balance_factor > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance_factor < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def remove(self, key):
        if not self.root:
            return

        self.root = self._remove(self.root, key)

    def removeById(self, key, Id):
        self._remove_by_id_recursive(key, self.root, Id)

    def _remove_by_id_recursive(self, key, current_node, Id):
        if current_node is None:
            return current_node

        if key < current_node.key.model:
            current_node.left = self._remove_recursive(key, current_node.left, Id)
        elif key > current_node.key.model:
            current_node.right = self._remove_recursive(key, current_node.right, Id)
        else:
            current_node.key.delete(Id)

    def _remove(self, node, key):
        if not node:
            return node

        if key < node.key.model:
            node.left = self._remove(node.left, key)
        elif key > node.key.model:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._find_min_node(node.right)
                node.key = min_node.key
                node.right = self._remove(node.right, min_node.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance_factor = self._get_balance(node)

        if balance_factor > 1:
            if self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance_factor < -1:
            if self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, key, Id=None):
        return self._search(self.root, key, Id)

    def _search(self, node, key, Id=None):
        if Id == None:
            if not node or node.key.model == key:
                if not node:
                    return print("O nó não existe")
                return node.key.show()

            if key < node.key.model:
                return self._search(node.left, key)
            else:
                return self._search(node.right, key)
        else:
            if not node or node.key.model == key:
                return node.key.show(Id)
            if key < node.key:
                return self._search(node.left, key)
            else:
                return self._search(node.right, key)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, p):
        z = p.right
        T2 = z.left

        z.left = p
        p.right = T2

        p.height = 1 + max(self._get_height(p.left), self._get_height(p.right))
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))

        return z

    def _rotate_right(self, p):
        u = p.left
        T3 = u.right

        u.right = p
        p.left = T3

        p.height = 1 + max(self._get_height(p.left), self._get_height(p.right))
        u.height = 1 + max(self._get_height(u.left), self._get_height(u.right))

        return u

    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def print_tree(self):
        if not self.root:
            print("A árvore está vazia.")
        else:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.key)
            self._print_tree(node.right)
