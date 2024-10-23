
import sqlite3
import json


def GeradorDB():
    # Criar um novo banco de dados SQLite (ou conectar se já existir)
    conexao = sqlite3.connect('Loja.db')
    return conexao


def CarregarTabela(conexao,df):
   
    # Criar a tabela a partir do DataFrame
    df.to_sql('temp_produtos', conexao, if_exists='replace', index=False)
    try:
    
        query_create_if_not_exist = f"""

            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY,
                name TEXT,
                value FLOAT,
                date DATE
            );
            """
        
        cursor = conexao.cursor()
        cursor.execute(query_create_if_not_exist)
        conexao.commit()
    except Exception as e :
        print(e)
        print("tabela produto ja existe")    

    query_insert = f""" 
          INSERT INTO produtos
            (
                id,
                name,
                value,
                date
            )
            SELECT 
                temp_produtos.id,
                temp_produtos.name,
                temp_produtos.value,
                temp_produtos.date
            FROM temp_produtos 
            LEFT JOIN produtos  ON
                temp_produtos.id = produtos.id
            WHERE produtos.id IS NULL;
            
            """
    cursor = conexao.cursor()
    cursor.execute(query_insert)
    conexao.commit()


    query_update = f""" 
            UPDATE produtos
            SET 
                name = (SELECT temp.name FROM temp_produtos temp WHERE temp.id = produtos.id),
                value = (SELECT temp.value FROM temp_produtos temp WHERE temp.id = produtos.id),
                date = (SELECT temp.date FROM temp_produtos temp WHERE temp.id = produtos.id)
            WHERE EXISTS (SELECT 1 FROM temp_produtos temp WHERE temp.id = produtos.id);
                """
    cursor = conexao.cursor()
    cursor.execute(query_update)
    conexao.commit()
    



    return "tabela carregada"



def ListarProduto(conexao, id):
    query = f"select * from produtos WHERE id = {id};"
    cursor = conexao.cursor()
    cursor.execute(query)
    registro = cursor.fetchall()
    # retornar um json ao inves de um objeto sqlite 
    colunas = [desc[0] for desc in cursor.description]
    registro= [dict(zip(colunas, linha)) for linha in registro]
    registro = json.dumps(registro, indent=4)
    
    return registro
    
def ListarTodosProdutos(conexao):
    query = "select * from produtos;"
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


