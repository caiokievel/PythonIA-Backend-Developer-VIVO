# TODO: Crie uma classe UsuarioTelefone.
class UsuarioTelefone:
    def __init__(self, nome, numero, plano) -> None:
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    @property
    def nome(self):
        return self.__nome

    @property
    def numero(self):
        return self.__numero

    @property
    def plano(self):
        return self.__plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()
numero = input()
plano = input()
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome=nome, numero=numero, plano=plano)
print(usuario)
