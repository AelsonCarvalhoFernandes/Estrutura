# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:02:16 2023

@author: fabio
"""

from bst import BinarySearchTree

# Criar uma instância da árvore binária de busca
bst = BinarySearchTree()

# Inserir chaves na árvore
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Realizar o percurso inorder
print("Inorder traversal:")
bst.inorder_traversal()

# Realizar o percurso preorder
print("Preorder traversal:")
bst.preorder_traversal()

# Realizar o percurso postorder
print("Postorder traversal:")
bst.postorder_traversal()

# Procurar uma chave na árvore
result = bst.search(40)
if result:
    print("Chave encontrada!")
else:
    print("Chave não encontrada!")

# Remover uma chave da árvore
bst.remove(30)

# Realizar o percurso inorder após a remoção
print("Inorder traversal após remoção:")
bst.inorder_traversal()
