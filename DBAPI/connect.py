import sqlite3
from pathlib import Path

ROOT_PATCH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATCH/'meu_banco.db')
