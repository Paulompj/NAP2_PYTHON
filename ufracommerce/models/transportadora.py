from .item import Item


class Transportadora:
    def __init__(self, nome: str, precoVolume: float, precoPeso: float, prazoDeEntrega: int):
        self.nome = nome
        self.precoVolume = precoVolume
        self.precoPeso = precoPeso
        self.prazoDeEntrega = prazoDeEntrega

    def calcularFrete(self, itens: list[Item]) -> float:
        frete_total = 0
        for item in itens:
            preco_por_volume = item.produto.volume * self.precoVolume * item.quantidade
            preco_por_peso = item.produto.peso * self.precoPeso * item.quantidade
            frete_total += max(preco_por_volume, preco_por_peso)
        return frete_total

    def __str__(self):
        return f"{self.nome} - Prazo de Entrega: {self.prazoDeEntrega} dias"
