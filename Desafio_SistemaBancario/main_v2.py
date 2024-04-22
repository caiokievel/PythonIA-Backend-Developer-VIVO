def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor < 0:
        print('Operação falhou! o valor informado é invalido.')
        
    elif numero_saques == limite_saques:
        print('Operação falhou! Limite de saques atingido.')

    elif valor <= limite:
        if valor <= saldo:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saques += 1
        else:
            print("Não foi possivel realizar o saque! Saldo insuficiente")
    else:
        print('Saque ultrapassou valor maximo.')
        
    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /,):
    
    if valor < 0:
        print('Operação falhou! o valor informado é invalido.')
    else:    
        saldo += valor
        extrato += f'Deposito: R${valor:.2f}\n'

    return saldo, extrato
    
def cria_extrato(saldo, /, *, extrato):
    print('\n##################### EXTRATO #####################')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('\n###################################################')

def formata_cpf(cpf):
    cpf_formatado = cpf.replace('.', '')
    cpf_formatado = cpf_formatado.replace('-', '')
    
    return cpf_formatado
    
def criar_cliente(nome, data_nascimento, cpf, logradouro, numero, bairro, cidade, estado):
    global clientes
    cpf_formatado = formata_cpf(cpf)
    
    for usuario in clientes:
        if usuario['cpf'] == cpf_formatado:
            return f'ERRO: CPF JÁ CADASTRADO!'
    else:
        endereço = f'{logradouro}, {numero} - {bairro} - {cidade}/{estado}'
        cliente = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf_formatado, 'endereço': endereço}
        clientes.append(cliente)
        return f'Cliente {cliente['nome']}, cadastrado com sucesso!'

def criar_conta_corrente(lista_clientes, agencia, numero_conta, cpf):
    global contas
    cpf_formatado = formata_cpf(cpf)
    
    for usuario in lista_clientes:
        if cpf_formatado == usuario['cpf']:
            usuario = usuario['nome']
            conta_corrente = {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
            contas.append(conta_corrente)
            return f'AGENCIA: {agencia}\nCONTA CORRENTE: {numero_conta}\n\n Conta cadastrada com sucesso!'
    
    return f'ERRO! usuario não encontrado!'

def listar(lista):
    print(lista)

clientes = []
contas = []
menu_inicial = """

[0] - Conectar
[1] - Novo cliente
[2] - Nova conta corrente
[3] - Listar clientes
[4] - Listar contas
[9] - Sair   

=> """

menu_cliente = """

[d] - Deposito
[s] - Saque
[e] - Extrato
[q] - Sair   

=> """

saldo = 2000
extrato = ''
qtd_saque = 0
numero_sequencial_conta = 1

LIMITE_DIARIO = 3
SAQUE_MAXIMO = 500
AGENCIA = '0001'

while True:
    
    opcao_menu_inicial = input(menu_inicial)
    
    if opcao_menu_inicial == '0':
        
        cpf_usuario = input('Informe seu cpf: ')
        conta_usuario = input('Informe sua conta: ')
        
        while True:
            
            opcao = input(menu_cliente)
            
            if opcao.lower() == 'd':
                valor = float(input('Digite o valor a ser depositado: '))
                
                saldo_deposito, extrato_deposito = deposito(saldo, valor, extrato)
                saldo = saldo_deposito
                extrato = extrato_deposito
                    
            elif opcao.lower() == 's':
                valor = int(input('Digite o valor a ser sacado: '))
                
                saldo_saque, extrato_saque, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=SAQUE_MAXIMO, numero_saques=qtd_saque, limite_saques=LIMITE_DIARIO)      
                saldo = saldo_saque   
                extrato = extrato_saque
                qtd_saque = numero_saques   
                
            elif opcao.lower() == 'e':
                cria_extrato(saldo, extrato=extrato)
                            
            elif opcao.lower() == 'q':
                break
            
            else:
                print('Operação invalida, por favor selecione novamente a operação desejada.')
    elif opcao_menu_inicial == '1':
        print('Bem-vindo ao menu novo cliente')
        
        print('########### Dados Pessoais ###########')
        nome = input('Informe seu nome: ')
        data_nascimento = input('Informe sua data de nascimento[DD/MM/AAAA]: ')
        cpf = input('Informe seu CPF: ')
        
        print('########### Endereço ###########')
        logradouro = input('Logradouro: ')
        numero = input('Numero: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado[SIGLA]: ')
        
        retorno = criar_cliente(nome, data_nascimento, cpf, logradouro, numero, bairro, cidade, estado)
        print(retorno)
        
    elif opcao_menu_inicial == '2':
        if clientes:
            cp_clientes = clientes.copy()
            
            print('Bem-vindo ao menu nova conta')
            print('########### Nova conta ###########')
            cpf = input('Informe seu CPF: ')
            
            if contas:
                numero_sequencial_conta = contas[-1]['numero_conta'] + 1
                print(numero_sequencial_conta)
                retorno = criar_conta_corrente(lista_clientes=cp_clientes, agencia=AGENCIA, numero_conta=numero_sequencial_conta, cpf=cpf)
                print(retorno)
            else:
                retorno = criar_conta_corrente(lista_clientes=cp_clientes, agencia=AGENCIA, numero_conta=1, cpf=cpf)
                print(retorno)
        else:
            print('ERRO! Nenhum usuario criado!')
        
    elif opcao_menu_inicial == '3':
        listar(clientes)
    elif opcao_menu_inicial == '4':
        listar(contas)
    elif opcao_menu_inicial == '9':
        break
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')