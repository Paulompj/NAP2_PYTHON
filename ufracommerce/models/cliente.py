class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nome} - E-mail: {self.email}"
