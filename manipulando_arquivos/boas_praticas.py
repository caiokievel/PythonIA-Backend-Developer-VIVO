from pathlib import Path

ROOT_PATCH = Path(__file__).parent

try:
    with open(ROOT_PATCH/'lorem.txt', 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f'Erro ao abrir o arquivo {exc}')
