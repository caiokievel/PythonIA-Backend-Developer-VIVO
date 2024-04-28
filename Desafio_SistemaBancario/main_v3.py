from abc import ABC, abstractmethod


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @saldo.getter
    def saldo(self):
        return self._saldo

    def nova_conta(self):
        pass

    def sacar(self, value):
        if self._saldo < value:
            return False
        else:
            return True

    def depositar(self, value):
        if value > 0:
            ...

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques


class Cliente:
    def __init__(self, endereco, contas) -> None:
        self._endereco = endereco
        self._contas = contas

    @property
    def endereco(self):
        pass

    @property
    def contas(self):
        pass

    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        pass


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas=None) -> None:
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'


class Historico:
    def adicionar_transacao(self, transacao):
        pass


class Transacao(ABC):
    @abstractmethod
    def registrar(self, valor):
        pass


class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    def registrar(self, valor):
        ...


class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    def registrar(self, valor):
        ...


def main():
    p1 = PessoaFisica(86237403000, 'Caio Kievel', 18031996,
                      'Av. João Ferreira Jardim, 138')

    conta1 = Conta(1000.00, 1, '0001', p1, None)
    saldo = conta1.saldo
    print(saldo)


main()
