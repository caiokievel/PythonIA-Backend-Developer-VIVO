class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p2 = Pessoa.criar_apartir_data_nascimento(1996, 3, 18, 'Caio')
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(17))
