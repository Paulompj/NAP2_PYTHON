class Endereco:
    def __init__(self, nome: str, logradouro: str, numero: str, complemento: str = ""):
        self.nome = nome
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento

    def __str__(self):
        return f"{self.nome}: {self.logradouro}, {self.numero} {self.complemento}"
