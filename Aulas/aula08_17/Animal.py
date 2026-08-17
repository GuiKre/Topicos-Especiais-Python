class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.esta_vivo = True

    def emitir_som(self):
        print("roar")

    def apresentar(self):
        print(f"Animal -> {self.nome}, {self.esta_vivo}")

class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade

    def emitir_som(self):
        print("miau")

    def apresentar(self):
        print(f"Gato -> {self.nome}, {self.esta_vivo}")

gato = Gato("Shrek", 8)
gato.emitir_som()
gato.apresentar()

cachorro = Animal("Tobias")
cachorro.emitir_som()
cachorro.apresentar()