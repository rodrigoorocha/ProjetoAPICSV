import pandas as pd

def read_csv_to_dataframe(file_path):
    """
    Lê um arquivo CSV e retorna um DataFrame do pandas.

    Args:
        file_path (str): O caminho do arquivo CSV a ser lido.

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados do arquivo CSV.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

