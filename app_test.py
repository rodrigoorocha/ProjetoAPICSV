import pytest
import pandas as pd
from io import StringIO
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_upload_csv(client):
    # Cria um arquivo CSV simulado para upload
    data = "id,nome,preco\n1,Produto 1,10.0\n2,Produto 2,20.0\n"
    file = (StringIO(data), "test.csv")

    # Envia a requisição de upload
    response = client.post("/upload", data={"file": file}, content_type="multipart/form-data")

    assert response.status_code == 200
    assert "sucesso" in response.get_json()  # Ajuste conforme a resposta esperada

def test_pegar_todos(client, mocker):
    # Mock da função ListarTodosProdutos
    mocker.patch("app.service.data_base_functions.ListarTodosProdutos", return_value=[{"id": 1, "nome": "Produto 1"}])
    
    response = client.get("/data")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)  # Verifica se retorna uma lista

def test_pegar_por_id(client, mocker):
    # Mock da função ListarProduto
    produto_id = 1
    mocker.patch("app.service.data_base_functions.ListarProduto", return_value={"id": produto_id, "nome": "Produto 1"})
    
    response = client.get(f"/data/{produto_id}")
    assert response.status_code == 200
    assert response.get_json().get("id") == produto_id
