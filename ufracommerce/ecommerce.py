from ufracommerce.models.cliente import Cliente
from ufracommerce.models.transportadora import Transportadora
from ufracommerce.models.pedido import Pedido


class ECommerce:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.pedidos = []
        self.transportadoras = []

    def pagar(self, pedido: Pedido, valor: float, voucher: str = None) -> bool:
        desconto = 0.1 if voucher else 0
        valor_total = pedido.total * (1 - desconto)
        if valor >= valor_total:
            print("Pagamento realizado com sucesso!")
            return True
        else:
            print("Pagamento insuficiente.")
            return False

    def cadastrar(self, cliente: Cliente):
        self.clientes.append(cliente)

    def comprar(self, produto):
        self.produtos.append(produto)

    def credenciar(self, transportadora: Transportadora):
        self.transportadoras.append(transportadora)

    def __str__(self):
        return f"ECommerce com {len(self.produtos)} produtos, {len(self.clientes)} clientes, {len(self.pedidos)} pedidos."
