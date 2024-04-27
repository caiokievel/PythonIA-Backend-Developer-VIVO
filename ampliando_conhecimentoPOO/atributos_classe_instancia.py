class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


a1 = Estudante('Caio', 1)
a2 = Estudante('Paula', 2)

mostrar_valores(a1, a2)

Estudante.escola = 'Python'

a3 = Estudante('Scooby', 3)

mostrar_valores(a1, a2, a3)
