linguagens = {'python', 'java', 'python'}

for i, l in enumerate(linguagens):
    print(f'INDICE: {i}, VALOR:{l}')

# {}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

x = conjunto_a.union(conjunto_b)

print(x)

# {}.intersection

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

x = conjunto_a.intersection(conjunto_b)

print(x)

# {}.difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

x = conjunto_a.difference(conjunto_b)
y = conjunto_b.difference(conjunto_a)

print(x)
print(y)

# {}.symmetric_difference

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

x = conjunto_a.symmetric_difference(conjunto_b)

print(x)

# {}.issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

x = conjunto_a.issubset(conjunto_b)
y = conjunto_b.issubset(conjunto_a)

print(x)
print(y)

# {}.issuperset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

x = conjunto_a.issuperset(conjunto_b)
y = conjunto_b.issuperset(conjunto_a)

print(x)
print(y)

# {}.isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

x = conjunto_a.isdisjoint(conjunto_b)
y = conjunto_a.isdisjoint(conjunto_c)

print(x)
print(y)

# {}.add

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

# {}.clear

sorteio = {1, 23}

sorteio.clear()

print(sorteio)

# {}.copy

sorteio = {1, 23}

sorteio.copy()

print(sorteio)

# {}.discard

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.discard(1)
print(numeros)
numeros.discard(45)
print(numeros)

# {}.pop

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.pop()
print(numeros)
numeros.pop()
print(numeros)

# {}.remove

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)

numeros.remove(1)
print(numeros)
#numeros.remove(45)
print(numeros)
