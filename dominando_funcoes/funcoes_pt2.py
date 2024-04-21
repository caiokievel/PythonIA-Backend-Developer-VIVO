"""Parametros especiais
    
    def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
            |             |                     | 
            |         Positional or keyword     |
            |                                   - Keyword only
             -- Positional only
"""
# Positional only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

# Keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

criar_carro(modelo='Palio', ano=1999, placa='ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')

# Keyword and position only

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

print()
criar_carro('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustivel='Gasolina')
criar_carro('Palio', 1999, 'ABC-1234', 'Fiat', motor='1.0', combustivel='Gasolina')
print()

"""Objetos de primeira classe
"""

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operacao {a} + {b} = {resultado}')
    
exibir_resultado(10, 10, somar)
print()

"""escopo global
"""

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))
