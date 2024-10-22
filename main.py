from gerador_csv import GeradorCSV
from extrator_csv import read_csv_to_dataframe
from data_base_functions import GeradorDB, CarregarTabela, EncerraDB, ListarTodosProdutos, ListarProduto

csv_path = GeradorCSV()

df = read_csv_to_dataframe(csv_path)
conexao = GeradorDB()
tabela = CarregarTabela(conexao, df)
produtos = ListarTodosProdutos(conexao)
#produto = ListarProduto(conexao, 2)
#print(produtos)








EncerraDB(conexao)


