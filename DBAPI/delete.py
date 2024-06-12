import sqlite3
from pathlib import Path

ROOT_PATCH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATCH/'meu_banco.db')

cursor = con.cursor()


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


deletar_registro(conexao=con, cursor=cursor, id=1)
