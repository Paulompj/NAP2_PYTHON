from .produto import Produto


class Item:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = 0
        self.calcularSubtotal()

    def calcularSubtotal(self):
        self.subtotal = self.produto.preco * self.quantidade

    def setQuantidade(self, quantidade: int):
        self.quantidade = quantidade
        self.calcularSubtotal()

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade} - Subtotal: R$ {self.subtotal:.2f}"
