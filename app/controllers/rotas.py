import pandas as pd
from app import app
from flask import request, jsonify
from app.service.data_base_functions import  CarregarTabela, ListarTodosProdutos ,ListarProduto 




@app.route("/upload", methods = ["POST"])
def upload():  
    """
    Example endpoint returning a hello world message
    ---
    responses:
      200:
        description: A successful response
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
    Example endpoint returning a hello world message
    ---
    responses:
      200:
        description: A successful response
    """
    return ListarTodosProdutos() , 200 


@app.route("/data/<id>", methods = ["GET"])
def pegar_por_id(id):
    """
    Example endpoint returning a hello world message
    ---
    responses:
      200:
        description: A successful response
    """
    return ListarProduto(id), 200 