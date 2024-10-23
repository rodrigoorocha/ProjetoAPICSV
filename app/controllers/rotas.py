import pandas as pd
from app import app
from flask import request, jsonify
from app.service.data_base_functions import  CarregarTabela, ListarTodosProdutos ,ListarProduto 




@app.route("/upload", methods = ["POST"])
def upload():  
    """
    Carrega um aquivo csv e insere no banco
    ---
    consumes:
      - multipart/form-data
    tags:
      - Registro  
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: O arquivo csv para upload
    responses:
      200:
        description: File uploaded successfully with content displayed
      400:
        description: Invalid file type or upload error
      500:
        description: Internal server error
    """
    if len(request.files) == 0 :
        return jsonify({"erro": "nao foi econtrado aquivo na requisicao"}), 400
    # objeto (ImmutableMultiDict) pega o csv dentro desse obj
    file = list(request.files.values())[0]

    if file.filename == "":
        return jsonify({"erro": "sem arquivo selecionado"}), 400
    
    if not file.filename.endswith(".csv") :
        return jsonify({"erro": "arquivo nao é um csv"}), 400
    
    df = pd.read_csv(file)
    

    return jsonify({"sucesso" : CarregarTabela(df)}), 200 


@app.route("/data", methods = ["GET"])
def pegar_todos():
    """
   Rota para buscar todos os Registro cadastrados
    ---
    tags:
      - Registro
    responses:
      200:
        description: A successful response
    """
    return ListarTodosProdutos() , 200 


@app.route("/data/<id>", methods = ["GET"])
def pegar_por_id(id):
    """
    Rota para buscar Registro pelo ID
    ---
    tags:
      - Registro
    parameters:
      - name: id
        in: path
        type: string
        required: True
        description: ID do Registro que deseja buscar
    responses:
      200:
        description: Registro listado com sucesso
      400:
        description: Erro de requisição, o ID fornecido é inválido
    """
    
    return ListarProduto(id), 200 