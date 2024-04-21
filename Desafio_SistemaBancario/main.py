menu = """

[d] - Deposito
[s] - Saque
[e] - Extrato
[q] - Sair   

=> """

saldo = 2000
extrato = ''
qtd_saque = 0

LIMITE_DIARIO = 3
SAQUE_MAXIMO = 500

while True:
    
    opcao = input(menu)
    
    if opcao.lower() == 'd':
        valor = float(input('Digite o valor a ser depositado: '))
        
        if valor < 0:
            print('Operação falhou! o valor informado é invalido.')
            continue
        
        saldo += valor
        
        extrato += f'Deposito: R${valor:.2f}\n'
    
    elif opcao.lower() == 's':
        valor = int(input('Digite o valor a ser sacado: '))
        
        if valor < 0:
            print('Operação falhou! o valor informado é invalido.')
            continue
        
        if qtd_saque == 3:
            print('Operação falhou! Limite de saques atingido.')
            continue

        if valor <= SAQUE_MAXIMO:
            if valor <= saldo:
                saldo -= valor
                extrato += f'Saque: R${valor:.2f}\n'
            else:
                print("Não foi possivel realizar o saque! Saldo insuficiente")
                continue
        else:
            print('Saque ultrapassou valor maximo.')
            continue
        
        qtd_saque += 1
    
    elif opcao.lower() == 'e':
        print('\n##################### EXTRATO #####################')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n###################################################')
        
        
    elif opcao.lower() == 'q':
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
        continue
    