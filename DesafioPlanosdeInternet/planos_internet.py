def recomendar_plano(consumo):
    plano_essencial = 'Plano Essencial Fibra - 50Mbps'
    plano_prata = 'Plano Prata Fibra - 100Mbps'
    plano_premium = 'Plano Premium Fibra - 300Mbps'
    
    if consumo < 10.1:
        return plano_essencial
    elif consumo < 20.1:
        return plano_prata
    else:
        return plano_premium 

consumo = float(input('Informe seu consumo medio: '))

print(recomendar_plano(consumo))
