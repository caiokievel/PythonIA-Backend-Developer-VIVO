

try:
    arquivo = open('meuarquivo.py')
except FileNotFoundError as exc:
    print('Arquivo não encontrado')
    print(exc)
