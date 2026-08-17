class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def _apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos!")

pessoa1 = Pessoa("João", 20)
pessoa1._apresentar()

pessoa2 = Pessoa("Krelling", 25)
pessoa2._apresentar()