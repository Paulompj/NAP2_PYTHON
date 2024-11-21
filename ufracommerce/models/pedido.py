from datetime import datetime
from .item import Item
from .transportadora import Transportadora


class Pedido:
    def __init__(self, cliente, endereco):
        self.dataHora = datetime.now()
        self.subtotal = 0
        self.frete = 0
        self.total = 0
        self.cliente = cliente
        self.endereco = endereco
        self.transportadora = None
        self.itens = []

    def adicionar(self, quantidade: int, produto):
        for item in self.itens:
            if item.produto == produto:
                item.setQuantidade(item.quantidade + quantidade)
                self.calcularTotal()
                return
        novo_item = Item(produto, quantidade)
        self.itens.append(novo_item)
        self.calcularTotal()

    def setTransportadora(self, transportadora: Transportadora):
        self.transportadora = transportadora
        self.calcularFrete()
        self.calcularTotal()

    def calcularFrete(self):
        if self.transportadora:
            self.frete = self.transportadora.calcularFrete(self.itens)

    def calcularTotal(self):
        self.subtotal = sum(item.subtotal for item in self.itens)
        self.total = self.subtotal + self.frete

    def __str__(self):
        return (
            f"Pedido de {self.cliente.nome} em {self.dataHora}\n"
            f"Subtotal: R$ {self.subtotal:.2f}\nFrete: R$ {self.frete:.2f}\nTotal: R$ {self.total:.2f}"
        )
