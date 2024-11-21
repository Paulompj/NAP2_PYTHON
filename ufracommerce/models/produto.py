class Produto:
    def __init__(self, nome: str, preco: float, volume: float, peso: float):
        self.nome = nome
        self.preco = preco
        self.volume = volume
        self.peso = peso

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} - Volume: {self.volume}m³ - Peso: {self.peso}kg"
