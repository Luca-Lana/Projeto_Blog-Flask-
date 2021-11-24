import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


# g é um objeto especial unico de cada requisição.
# è usado  para armazernar dado que vai ser usado em multiplas funções durante a requisição
# assim nele vai ser armazena a conexao com o banco caso necessario reusar
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # fala pra conexão retornar linhas  que se comportam como dict. Isso permite acessar as colunas pr nome
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Limpa os dados existentes e cria novas tabelaas"""
    init_db()
    click.echo('Initialized the database.')

# as funções close_db e init_db precisam ser registradas para ser usadas
# mas como nos estamos usando factory function isso não esta disponivel 
# então escrevemos a função init_app que recebe o app e faz o registro
def init_app(app):
    app.teardown_appcontext(close_db) # fala pro flask chamar essa função antes de enviar a resposta
    app.cli.add_command(init_db_command) # adiciona um novo comando q  vai ser chamado com o comando do flask