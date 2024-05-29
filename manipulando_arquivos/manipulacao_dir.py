import os
import shutil
from pathlib import Path

ROOT_PATCH = Path(__file__).parent

# os.mkdir(ROOT_PATCH / "novo-diretorio")

arquivo = open(ROOT_PATCH / 'novo-arquivo.txt', 'w')
arquivo.close()

os.rename(ROOT_PATCH/'novo-arquivo.txt', ROOT_PATCH/'arquivo.txt')

# os.remove(ROOT_PATCH/'arquivo.txt')

shutil.move(ROOT_PATCH/'arquivo.txt', ROOT_PATCH /
            'novo-diretorio'/'arquivo.txt')
