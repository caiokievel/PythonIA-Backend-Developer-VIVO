class MeuIterador:
    def __init__(self, numeros: list[int]) -> None:
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


list = [1, 2, 3, 4]

for i in MeuIterador(list):
    print(i)
