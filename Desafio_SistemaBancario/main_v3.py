from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
import textwrap
from datetime import datetime


class Conta:
    def __init__(self, numero, cliente):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def cliente(self):
        return self.__cliente

    @property
    def historico(self):
        return self.__historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, value):
        saldo = self.__saldo
        execedeu_saldo = value > saldo

        if execedeu_saldo:
            print('\n@@@ Operação Falhou! Saldo insuficiente! @@@')
        elif value > 0:
            self.__saldo -= value
            print('\n=== Saque realizado com sucesso! ===')
            return True
        else:
            print('\n@@@ Operação Falhou! Valor invalido! @@@')

        return False

    def depositar(self, value):
        if value > 0:
            self.__saldo += value
            print('\n=== Deposito realizado com sucesso! ===')
        else:
            print('\n@@@ Operação Falhou! Valor invalido! @@@')

            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.__limite = limite
        self.__limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self.__limite
        excedeu_saques = numero_saques >= self.__limite_saques

        if excedeu_limite:
            print('\n@@@ Operação Falhou! O valor do saque excedeu o limite! @@@')

        elif excedeu_saques:
            print('\n@@@ Operação Falhou! Numero de saques excedidos! @@@')

        else:
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco) -> None:
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Historico:
    def __init__(self) -> None:
        self.__transcacoes = []

    @property
    def transacoes(self):
        return self.__transcacoes

    def adicionar_transacao(self, transacao):
        self.__transcacoes.append({"tipo": transacao.__class__.__name__,
                                   "valor": transacao.valor,
                                   "data": datetime.now()})


class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.__valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.__valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu_inicial = """
    ====== MENU ======
    [0] - Deposito
    [1] - Saque
    [2] - Extrato
    [3] - Nova conta
    [4] - Listar contas
    [5] - Novo Usuario
    [9] - Sair   
    ==================

    => """

    return input(textwrap.dedent(menu_inicial))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [
        cliente for cliente in clientes if cliente.cpf == cpf]

    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\n@@@ Cliente não possui conta! @@@')
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")

    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não existe! @@@')
        return

    valor = float(input('Informe o valor a ser depositado: '))

    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não existe! @@@')
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não existe! @@@')
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    print('\n=================== EXTRATO ===================')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas operaçoes'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}'

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('\n==============================================')


def criar_cliente(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\n@@@ Cliente já existe! @@@')
        return

    nome = input('Informe o nome completo: ')

    data_nascimento = input('Informe a data de nacimento(dd-mm-aaaa): ')

    endereco = input('Informe o endereço: ')

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print('\nCliente criado com sucesso!')


def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não existe! @@@')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta criada com sucesso!')


def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 0:
            depositar(clientes)
        elif opcao == 1:
            sacar(clientes)
        elif opcao == 2:
            exibir_extrato(clientes)
        elif opcao == 3:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == 4:
            listar_contas(contas)
        elif opcao == 5:
            criar_cliente(clientes)
        elif opcao == 9:
            break
        else:
            print('\nOperação invalida')


main()
