
import sqlite3
import json


def GeradorDB():
    # Criar um novo banco de dados SQLite (ou conectar se já existir)
    conexao = sqlite3.connect('Loja.db')
    return conexao


def CarregarTabela(conexao,df):
    # Criar a tabela a partir do DataFrame
    df.to_sql('produtos', conexao, if_exists='replace', index=False)
    return "tabela carregada"

def ListarProduto(conexao, id):
    query = f"select * from produtos WHERE id = {id}"
    cursor = conexao.cursor()
    cursor.execute(query)
    registro = cursor.fetchall()
    # retornar um json ao inves de um objeto sqlite 
    colunas = [desc[0] for desc in cursor.description]
    registro= [dict(zip(colunas, linha)) for linha in registro]
    registro = json.dumps(registro, indent=4)
    return registro
    
def ListarTodosProdutos(conexao):
    query = "select * from produtos"
    cursor = conexao.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    # retornar um json ao inves de um objeto sqlite 
    colunas = [desc[0] for desc in cursor.description]
    registros= [dict(zip(colunas, linha)) for linha in registros]
    registros = json.dumps(registros, indent=4)
    return registros


def EncerraDB(conexao):
    # Fechar a conexão
    conexao.close()
    return "conexao encerrada"


