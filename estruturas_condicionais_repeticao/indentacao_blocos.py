saldo = 500

def sacar(valor: float):
    if saldo >= valor:
        print("valor sacado")
        print("reture o seu dinheiro na boca do caixa.")
        
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
    
def depositar(valor):
    saldo += valor
    
sacar(600)
