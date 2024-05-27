def dizer_oi(nome):
    return f'Oi {nome}'


def incentivar_aprender(nome):
    return f'Oi {nome}, vamos aprender python juntos!'


def mensagem_para_guilherme(funcao_mensagem):
    return funcao_mensagem('Guilherme')


x = mensagem_para_guilherme(dizer_oi)
y = mensagem_para_guilherme(incentivar_aprender)

print(x)
print(y)
