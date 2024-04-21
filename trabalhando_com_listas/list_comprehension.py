numeros = [1, 30, 21, 2, 9, 65, 34]

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros]

print(quadrado)

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print()
print(numeros)