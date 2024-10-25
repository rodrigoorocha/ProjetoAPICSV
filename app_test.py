
import pytest
import sqlite3
import json
import pandas as pd
from app.service.data_base_functions import GeradorDB, CarregarTabela, ListarProduto, ListarTodosProdutos, EncerraDB


@pytest.fixture
def sample_data():
    # Criar um DataFrame de amostra
    data = {
        "id": [1, 2],
        "name": ["Produto A", "Produto B"],
        "value": [100.0, 200.0],
        "date": ["2023-01-01", "2023-01-02"]
    }
    return pd.DataFrame(data)


@pytest.fixture
def setup_db(sample_data):
    conexao = GeradorDB()
    
    # Limpa a tabela produtos para garantir que não haja dados residuais
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos;")
    conexao.commit()
    
    # Carrega a tabela com o `sample_data`
    CarregarTabela(sample_data)
    yield conexao
    EncerraDB(conexao)


def test_CarregarTabela(setup_db):
    # Verifica se a tabela foi criada e carregada corretamente
    conexao = setup_db
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    registros = cursor.fetchall()
    
    assert len(registros) == 2  # Verifica que há 2 registros na tabela
    assert registros[0][1] == "Produto A"
    assert registros[1][1] == "Produto B"


def test_ListarProduto(setup_db):
    produto = ListarProduto(1)
    produto = json.loads(produto)
    
    # Verificar os dados do produto retornado
    assert produto['id'] == 1
    assert produto['name'] == "Produto A"
    assert produto['value'] == 100.0
    assert produto['date'] == "2023-01-01"


def test_ListarTodosProdutos(setup_db):
    produtos = ListarTodosProdutos()
    produtos = json.loads(produtos)
    
    # Verifica que a função retorna todos os produtos
    assert len(produtos) == 2
    assert produtos[0]['name'] == "Produto A"
    assert produtos[1]['name'] == "Produto B"


def test_EncerraDB():
    conexao = GeradorDB()
    EncerraDB(conexao)
    
    # Verifica se a conexão foi encerrada ao tentar usar um cursor após o fechamento
    with pytest.raises(sqlite3.ProgrammingError):
        conexao.cursor()  # Deve falhar se a conexão foi corretamente encerrada



