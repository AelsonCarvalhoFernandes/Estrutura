# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 23:10:47 2023

@author: fabio
"""

from avl_tree import AVLTree

tree = AVLTree()

# Inserção
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

# Impressão da árvore
print("Árvore AVL:")
tree.print_tree()
print()

# Pesquisa
key = 30
result = tree.search(key)
if result:
    print(f"A chave {key} foi encontrada na árvore.")
else:
    print(f"A chave {key} não foi encontrada na árvore.")
print()

# Remoção
key = 30
tree.remove(key)
print(f"Removendo a chave {key}...")
print("Árvore AVL após a remoção:")
tree.print_tree()
