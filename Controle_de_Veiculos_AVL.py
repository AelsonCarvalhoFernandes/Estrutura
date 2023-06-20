from Repositories.LinkedList.LinkedList import LinkedList
from Repositories.Car import Car
from Repositories.AVL.avl_tree import AVLTree

tree = AVLTree()

ligado = True

while ligado:
    print("Oque deseja fazer:\n[1] Inserir um veiculo\n[2] Alterar um veiculo\n[3] Ver veiculo\n[0] Excluir um veiculo")
    escolha = input("Escolha: ")
    if escolha == "1":

        modelo = int(input("Qual modelo deseja inserir:\n[1] Compacto\n[2] SUV\n[3] Picape\n[4] Esportivos\n[5] Caminhão\n[6] Colecionaveis\n[7] Carro de luxo\nEscolha: "))

        marca = input("Qual a marca do veiculo: ")
        ano = input("Qual o ano de fabricação do veiculo: ")
        preco = input("Qual o preço do veiculo: R$ ")

        lista = LinkedList(modelo)
        lista.append(Car(preco, ano, marca))

        tree.insert(lista)

    if escolha == "2":
        pass

    if escolha == "3":
        modelo = int(input("Qual modelo deseja pesquisar:\n[1] Compacto\n[2] SUV\n[3] Picape\n[4] Esportivos\n[5] Caminhão\n[6] Colecionaveis\n[7] Carro de luxo\nEscolha: "))
        tree.search(modelo, 2)
    
    if escolha == "0":
        print("Escolha o modelo e o ID, Se o ID não for inserido todo o modelo será apagado\n")
        modelo = int(input("Qual modelo deseja excluir:\n[1] Compacto\n[2] SUV\n[3] Picape\n[4] Esportivos\n[5] Caminhão\n[6] Colecionaveis\n[7] Carro de luxo\nModelo: "))
        Id = int(input("ID: "))

        if Id == None:
            tree.remove(modelo)
        else:
            tree.removeById(modelo, Id)