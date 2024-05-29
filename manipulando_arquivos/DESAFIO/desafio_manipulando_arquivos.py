from abc import ABC, abstractclassmethod, abstractmethod, abstractproperty
import textwrap
from datetime import datetime
from pathlib import Path
import os
import csv
ROOT_PATCH = Path(__file__).parent


def decorador_log(function):
    def envelope(*args, **kwargs):
        datetime_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        function_name = function.__name__
        resultado = function(*args, **kwargs)
        try:
            with open(ROOT_PATCH/'log.txt', 'a', encoding='utf-8') as file:
                file.write(f"[{datetime_now}] Função '{function_name}' executada com argumentos {
                           args} e {kwargs}. Retornou {resultado}\n")
        except IOError as error:
            print(error)

        print(f'Datetime: {datetime_now}, Type: {function_name}')
        return resultado
    return envelope


class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.contador]
            self.contador += 1
            print('=' * 100)
            return conta
        except IndexError:
            raise StopIteration


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

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

    def __str__(self) -> str:
        return textwrap.dedent(f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """)


class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        qtd_transacao_dia = len(conta.historico.transacoes_do_dia())

        if qtd_transacao_dia >= 10:
            print('\n@@@ Você excedeu o numero de transações permitidas para hoje! @@@')
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco) -> None:
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ({self.cpf})>"


class Historico:
    def __init__(self) -> None:
        self.__transcacoes = []

    @property
    def transacoes(self):
        return self.__transcacoes

    def adicionar_transacao(self, transacao):
        self.__transcacoes.append({"tipo": transacao.__class__.__name__,
                                   "valor": transacao.valor,
                                   "data": datetime.now().strftime('%d/%m/%Y %H:%M:%S'), })

    def gerador_relatorios(self, tipo=None):
        if not tipo:
            for transacao in self.transacoes:
                yield transacao
        if tipo:
            for transacao in self.transacoes:
                if transacao['tipo'] == tipo:
                    yield transacao

    def transacoes_do_dia(self):
        transacoes_dia = []
        for transacao in self.transacoes:
            dia_atual = datetime.now().strftime('%d/%m/%Y')
            if transacao['data'][:10] == dia_atual:
                transacoes_dia.append(transacao)

        return transacoes_dia


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


def menu_extrato():
    menu_extrato = """
    ===== Extrato =====
    [0] - Deposito
    [1] - Saque
    [2] - Saque e Deposito
    [9] - Voltar   
    ===================

    => """

    return input(textwrap.dedent(menu_extrato))


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


@decorador_log
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


@decorador_log
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


@decorador_log
def exibir_extrato(clientes, tipo):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\n@@@ Cliente não existe! @@@')
        return

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    print('\n=================== EXTRATO ===================')
    transacoes = conta.historico.gerador_relatorios(tipo)

    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas operaçoes'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']
                            }:\n\t{transacao['data']} R${transacao['valor']:.2f}'

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('\n==============================================')


@decorador_log
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
    escritor('usuarios.csv', nome=nome,
             data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    print('\nCliente criado com sucesso!')


@decorador_log
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
    for i in ContaIterador(contas):
        print(i)


def criar_csv(nome):
    if nome == 'usuarios':
        print('Criando CSV de USUARIOS...')
        try:
            with open(ROOT_PATCH/'usuarios.csv', 'w', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                escritor.writerow(
                    ['nome', 'data_nascimento', 'cpf', 'endereco'])
        except IOError as error:
            print(f'Erro ao criar o arquivo.\n{error}')


def escritor(arquivo, nome, data_nascimento, cpf, endereco):
    if arquivo == 'usuarios.csv':
        try:
            with open(ROOT_PATCH/'usuarios.csv', 'a', newline='', encoding='utf-8') as file:
                escritor = csv.writer(file)
                escritor.writerow([nome, data_nascimento, cpf, endereco])
        except IOError as exc:
            print(f'Erro ao criar o arquivo. {exc}')


def main():
    clientes = []
    contas = []

    try:
        with open(ROOT_PATCH/'usuarios.csv', 'r', newline='', encoding='utf-8') as file:
            print('Carregando clientes...')
            reader = csv.DictReader(file)

            for row in reader:
                cliente = PessoaFisica(
                    nome=row['nome'], data_nascimento=row['data_nascimento'], cpf=row['cpf'], endereco=row['endereco'])
                clientes.append(cliente)
    except IOError as error:
        print(error)
        criar_csv('usuarios')

    while True:
        opcao = int(menu())

        if opcao == 0:
            depositar(clientes)
        elif opcao == 1:
            sacar(clientes)
        elif opcao == 2:
            opcao_extrato = int(menu_extrato())
            if opcao_extrato == 0:
                exibir_extrato(clientes, 'Deposito')
            elif opcao_extrato == 1:
                exibir_extrato(clientes, 'Saque')
            elif opcao_extrato == 2:
                exibir_extrato(clientes, None)
            else:
                continue
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
