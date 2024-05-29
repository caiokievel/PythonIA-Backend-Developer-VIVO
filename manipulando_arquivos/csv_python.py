import csv
from pathlib import Path

ROOT_PATCH = Path(__file__).parent
try:
    with open(ROOT_PATCH/'usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')

try:
    with open(ROOT_PATCH/'usuarios.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')
