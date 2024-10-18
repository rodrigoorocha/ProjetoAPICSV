import csv
import random
from datetime import datetime, timedelta

def GeradorCSV ():
    # Definindo os parâmetros
    num_records = 20
    start_date = datetime(2024, 1, 1)

    path = 'produtos.csv'

    # Gerando os dados
    data = []
    for i in range(num_records):
        item_id = i + 1
        name = f"Item_{chr(65 + (i % 26))}"  # Gera nomes como Item A, Item B, etc.
        value = round(random.uniform(5.0, 20.0), 2)  # Gera valores aleatórios
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')  # Incrementa a data
        data.append([item_id, name, value, date])

    # Escrevendo no arquivo CSV
    with open( path ,'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'value', 'date'])  # Cabeçalhos
        writer.writerows(data)

    print(f"Arquivo '{path}' gerado com sucesso!")

    return path
