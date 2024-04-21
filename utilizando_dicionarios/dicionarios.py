pessoa = {'nome': 'Caio', 'idade': '28'}

pessoa = dict(nome='Caio', idade=28)

pessoa['telefone'] = '1234-1234'

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['telefone'])

# Dict aninhado

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-2223'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-2224', 'extra': {'a': 1} },
}

telefone = contatos['giovanna@gmail.com']['telefone']

print(telefone)

extra = contatos['melanie@gmail.com']['extra']['a']

print(extra)

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
