import mysql.connector

#definindo uma função que cria uma conexão com o banco de dados
def criar_conexao(host, usuario, senha, banco):
	return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

#Função para fechar a conexão com o bd
def fechar_conexao(conexao):
	return conexao.close()


