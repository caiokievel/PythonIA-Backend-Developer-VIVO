import sqlite3
from pathlib import Path

ROOT_PATCH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATCH/'meu_banco.db')

cursor = con.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)',
                   ('Teste 3', 'teste3@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?,?,?)',
                   (2, 'Teste 4', 'teste4@gmail.com'))
except Exception as err:
    print(f'Ops! um erro ocorreu {err}')
    con.rollback()
finally:
    con.commit()
