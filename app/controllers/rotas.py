from app import app
from flask import request, jsonfy


@app.route("/upload", methods = ["POST"])
def upload():
    if "file" not in request.files:
        return jsonfy({"erro": "nao foi econtrado aquivo na requisicao"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonfy({"erro": "sem arquivo selecionado"}), 400
    
    if not file.filename.endswith(".csv") :
        return jsonfy({"erro": "arquivo nao é um csv"}), 400
    
    return file


@app.route("/data", methods = ["GET"])
def pegar_todos():
    return


@app.route("/data/<id>", methods = ["GET"])
def pegar_por_id(id):
    return