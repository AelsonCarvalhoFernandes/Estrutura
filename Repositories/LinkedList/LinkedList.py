from .Node import Node

class LinkedList:
    def __init__(self, model):
        self.root = None
        self.model = model
        match self.model:
            case 1:
                self.modelName = "Compacto"
            case 2:
                self.modelName = "SUV"
            case 3:
                self.modelName = "Picape"
            case 4:
                self.modelName = "Esportivo"
            case 5:
                self.modelName = "Caminhão"
            case 6:
                self.modelName = "Carro de luxo"


    def append(self, value):
        if self.root == None:
            self.root = Node()
            self.root.value = value
            self.Id(self.root)
        else:
            self.recursiveAppend(self.root, value)

    def recursiveAppend(self, node, value):
        if node.value.price > value.price:
            if node.previous == None:
                self.root = Node()
                self.root.value = value
                self.root.next = node
                self.Id(self.root)
            else:
                node.previous.next = Node()
                node.previous.next.value = value
                node.previous.next.previous = node.previous
                self.Id(node)

        elif node.value.price < value.price:
            if node.next == None:
                node.next = Node()
                node.next.value = value
                node.next.previous = node
                print(node.next.previous)
                self.Id(node)
            else:
                self.recursiveAppend(node.next, value)
        elif node.value.price == value.price and node.value.year == value.year and node.value.brand == value.brand:
            print("O valor já se encontra na tabela")

    def Id(self, node):
        if node.previous == None:
            node.value.id = 1
            if node.next:
                self.Id(node.next)
        else:
            node.value.id = node.previous.value.id + 1
            if node.next:
                self.Id(node.next)


    def show(self, value = None):
        if self.root == None:
            print("Não existe nenhum veiculo")
        else:
            self.recursiveShow(self.root, value)


    def recursiveShow(self, node, Id=None):
        if Id is None:
            print(f"Modelo: {self.modelName} | ID: {node.value.id} | Marca: {node.value.brand} | Preço: R${node.value.price} | Ano: {node.value.year}")
            if node.next:
                self.recursiveShow(node.next)
        else:
            if node.value.id == Id:
                print(f"Modelo: {self.modelName} | ID: {node.value.id} | Marca: {node.value.brand} | Preço: R${node.value.price} | Ano: {node.value.year}")

            else:
                if node.next:
                    self.recursiveShow(node.next, Id)
                
                else:
                    print("O valor inserido não está na lista")

    def delete(self, id):
        if self.root == None:
            print(f"A lista de {self.modelName} está vazia")
        else:
            self.recursiveDelete(self.root, id)

    def recursiveDelete(self, node, Id):
        if node.value.id == Id:
            if node.next:
                if node.previous:
                    node.previous.next = node.next
                    self.Id(node.previous)
                else:
                    self.root = node.next
                    self.Id(node.previous.next)
            else:
                node.previous.next = None
        else:
            self.recursiveDelete(node.next, Id)
        