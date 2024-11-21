from .produto import Produto


class ProdutoCombo:
    def __init__(self, tipoDeDesconto: str, valorDoDesconto: float, produtos: list[Produto]):
        self.tipoDeDesconto = tipoDeDesconto
        self.valorDoDesconto = valorDoDesconto
        self.produtos = produtos

    def getPreco(self) -> float:
        preco_total = sum(produto.preco for produto in self.produtos)
        if self.tipoDeDesconto == "P":
            return preco_total * (1 - self.valorDoDesconto / 100)
        elif self.tipoDeDesconto == "V":
            return preco_total - self.valorDoDesconto
        return preco_total

    def __str__(self):
        return f"Combo com {len(self.produtos)} produtos - Preço: R$ {self.getPreco():.2f}"
