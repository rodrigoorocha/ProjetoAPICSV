# Objetivos do projeto

Esta API permite o upload de um arquivo CSV, que sera parseado para ser inserido em nosso banco de dados. 
Serão disponibilizados endpoints que permitam a consulta dos dados inseridos no banco.




# Pre requisistos 

 1. Utilizar a versão Python 3.13

 2. Recomendamos criação de um virtual environment conforme exemplo abaixo

     `pip install -r requirements.txt`
     `py -m venv venv`  
     `.\venv\Scripts\activate`
 


 3.  os frameworks instalados seguem abaixo  
  
     `Flask API`

     `pytest `

     

# Instruções para rodar a aplicação

1. ativar o virtual environment 
 `.\venv\Scripts\activate`



# Estrutura do projeto 

 1. app - Diretório principal da aplicação 
 
      a.  routes.py - rotas das chamdas dos endpoints

      b. data_base_functions.py - Inicializa o banco de dados(sqlite). Executa um sql script para criar a tabela item. Gerencia a conexao do banco de dados e faz faz as funçoes onde sera feito o upload e leitura por ai e leitira de todos os registros


 2. run.py - Onde toda o programa

 3. tests - Diretorio de testes unitários
 4. requirements.txt - Lista as dependências do projeto
 5. README.md - Documentação do projeto

# Funcionalidades
As funcionalidades abaixo serão desenvolvidas para nosso projeto.

## Upload de Arquivo CSV
- Para teste dessa funcionalidade podem gerar o arquivo com o a função de gerador 

- Acesse o endereço http://127.0.0.1:5000/upload. e envia o aruivo via postman



## Listar Todos os Registros

-  Acesse o endereço http://127.0.0.1:5000/data para retornar todos os registros armazenados no banco de dados

## Listar Registros por ID 

-  Acesse o endereço http://127.0.0.1:5000/data/{id} para retornar o registro selecionado por {id} armazenados no banco de dados

