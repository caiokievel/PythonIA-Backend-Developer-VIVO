import sqlite3
from pathlib import Path

ROOT_PATCH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATCH/'meu_banco.db')

cursor = con.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


def inserir_registro(conexao, cursor):
    data = ('Caio', 'caio@gmail.com')
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()


def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()


def inserir_many_registro(conexao, cursor):
    data = [('Caio', 'caio@gmail.com'), ('Caio_2', 'caio_2@gmail.com'),
            ('Caio_3', 'caio_3@gmail.com')]
    cursor.executemany(
        'INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes')


cliente = recuperar_cliente(cursor=cursor, id=2)
print(dict(cliente))
print(cliente['nome'])

clientes = listar_clientes(cursor=cursor)
for cliente in clientes:
    print(dict(cliente))
