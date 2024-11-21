from ufracommerce.ecommerce import ECommerce
from ufracommerce.models.produto import Produto
from ufracommerce.models.produto_combo import ProdutoCombo
from ufracommerce.models.cliente import Cliente
from ufracommerce.models.endereco import Endereco
from ufracommerce.models.pedido import Pedido
from ufracommerce.models.transportadora import Transportadora

if __name__ == "__main__":
    # Instanciar o sistema UFRACommerce
    ecommerce = ECommerce()

    # Criar produtos
    produto1 = Produto("Notebook", 4000, 0.02, 2)
    produto2 = Produto("Mouse", 100, 0.005, 0.1)
    produto3 = Produto("Teclado", 200, 0.01, 0.5)
    produto4 = Produto("Monitor", 170, 0.01, 0.7)
    produto5 = Produto("Fone de Ouvido", 80, 0.01, 0.3)


    # Criar combo de produtos
    combo1 = ProdutoCombo(
        "P", 10, [produto2, produto3]
    )  # Desconto percentual de 10%

    # Cadastrar cliente
    cliente1 = Cliente("João Silva", "joao@email.com")
    ecommerce.cadastrar(cliente1)
    cliente2 = Cliente("Lucas André", "laoplucas@email.com")
    ecommerce.cadastrar(cliente2)
    cliente3 = Cliente("Paulo Moraes", "pauloJaveiro@email.com")
    ecommerce.cadastrar(cliente3)

    # Criar endereço
    endereco1 = Endereco("Casa João", "Rua A", "123")
    endereco2 = Endereco("Casa do LaopLucas", "Rua B", "321")
    endereco3 = Endereco("Casa do Paulo", "Rua C", "213")

    # Criar pedido
    pedido1 = Pedido(cliente1, endereco1)
    pedido1.adicionar(1, produto1)
    pedido1.adicionar(2, produto2)

    pedido2 = Pedido(cliente2, endereco2)
    pedido2.adicionar(1, produto1)
    pedido2.adicionar(2, produto2)

    # Associar transportadora
    transportadora1 = Transportadora("Correios", 50, 30, 5)
    pedido1.setTransportadora(transportadora1)
    transportadora2 = Transportadora("Mercado Livre", 25, 70, 7)
    pedido2.setTransportadora(transportadora2)

    # Registrar pedido no sistema
    ecommerce.pedidos.append(pedido1)
    ecommerce.pedidos.append(pedido2)

    # Exibir pedido
    print(pedido1)
    print(pedido2)
