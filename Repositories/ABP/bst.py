from .node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(key, self.root)

    def _insert_recursive(self, key, current_node):
        if key.model < current_node.key.model:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(key, current_node.left)
        elif key.model == current_node.key.model:
            current_node.key.append(key.root.value)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(key, current_node.right)

    def search(self, key, Id=None):
        return self._search_recursive(key, self.root, Id)

    def _search_recursive(self, key, current_node, Id=None):
        if Id == None:
            if current_node is None or current_node.key.model == key:
                return current_node.key.show()
            if key < current_node.key.model:
                return self._search_recursive(key, current_node.left)
            return self._search_recursive(key, current_node.right)
        else:
            if current_node is None or current_node.key.model == key:
                return current_node.key.show(Id)
            if key < current_node.key.model:
                return self._search_recursive(key, current_node.left, Id)
            return self._search_recursive(key, current_node.right, Id)


    def remove(self, key):
        self.root = self._remove_recursive(key, self.root)
    
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

    def _remove_recursive(self, key, current_node):
        if current_node is None:
            return current_node

        if key < current_node.key:
            current_node.left = self._remove_recursive(key, current_node.left)
        elif key > current_node.key:
            current_node.right = self._remove_recursive(key, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            else:
                current_node.key = self._find_minimum(current_node.right)
                current_node.right = self._remove_recursive(current_node.key, current_node.right)
        return current_node

    def _find_minimum(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.key

    def inorder_traversal(self):
        self._inorder_recursive(self.root.key.show())

    def _inorder_recursive(self, current_node):
        if current_node:
            self._inorder_recursive(current_node.left)
            print(current_node.key)
            self._inorder_recursive(current_node.right)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, current_node):
        if current_node:
            print(current_node.key)
            self._preorder_recursive(current_node.left)
            self._preorder_recursive(current_node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, current_node):
        if current_node:
            self._postorder_recursive(current_node.left)
            self._postorder_recursive(current_node.right)
            print(current_node.key)
