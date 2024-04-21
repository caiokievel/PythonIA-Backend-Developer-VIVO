# {}.clear

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-2223'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-2224', 'extra': {'a': 1} },
}

contatos.clear()
print(contatos)

# {}.copy

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-2223'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-2224', 'extra': {'a': 1} },
}

copia = contatos.copy()
copia['guilherme@gmail.com'] = {'nome': 'Gui'}
print(contatos['guilherme@gmail.com'])
print(copia['guilherme@gmail.com'])

# {}.fromkeys

dict.fromkeys(['nome', 'telefone'])
dict.fromkeys(['nome', 'telefone'], 'vazio')

# {}.get

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

# contatos['chave'] # KeyError

x = contatos.get('chave')
y = contatos.get('chave', {})
z = contatos.get('guilherme@gmail.com', {})

print(x)
print(y)
print(z)

# {}.items

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

x = contatos.items()

print(x)

# {}.keys

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

x = contatos.keys()
y = contatos['guilherme@gmail.com'].keys()

print(x)
print(y)

# {}.pop

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

x = contatos.pop('guilherme@gmail.com')
y = contatos.pop('guilherme@gmail.com', 'Não encontrou')

print(x)
print(y)

# {}.popitem

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

x = contatos.popitem()


print(x)

# {}.setdefault

contatos = {'nome': 'Guilherme', 'telefone': '3333-2221'}

x = contatos.setdefault('idade', '28')

print(x)
print(contatos)

# {}.update

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
}

contatos.update({'guilherme@gmail.com': {'nome': 'Gui'}})
contatos.update({'giovanna@gmail.com': {'nome': 'Giovana'}})


print(contatos)

# {}.values

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-2223'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-2224', 'extra': {'a': 1} },
}

x = contatos.values()
print(x)

# {}.in

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-2223'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-2224', 'extra': {'a': 1} },
}

resultado = 'guilherme@gmail.com' in contatos
print(resultado)

resultado = 'megui@gmail.com' in contatos
print(resultado)

resultado = 'idade' in contatos['guilherme@gmail.com']
print(resultado)

resultado = 'telefone' in contatos['giovanna@gmail.com']
print(resultado)

# {}.del

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '3333-2223'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-2224', 'extra': {'a': 1} },
}

del contatos['guilherme@gmail.com']['telefone']
del contatos['chappie@gmail.com']

print(contatos)
