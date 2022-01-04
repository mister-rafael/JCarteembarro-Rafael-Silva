from model import *
	
def inserir(dados, tabela):
	try:
		tabela.insert_many(dados).execute()
		print("Dados inseridos com sucesso.")
	except:
		print("Há dados repetidos")
		return False
def remover():
	pass

def alterar():
	pass

def consultar(tabela):
	resultado = tabela.select()
	for i in resultado:
		print(i)
	

