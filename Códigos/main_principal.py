from classes import *
from conexao import * #importando tudo que tem em conexão

vendas = []

def cadastrarPeca(conexao, peca):
	if isinstance(peca, Peca):
		cursor = conexao.cursor()
		comando_sql = "INSERT INTO estoque_pecas (descrição, valorUnitario) values (%s, %s)"
		valores = (peca.nome, peca.valor)
		cursor.execute(comando_sql, valores)
		cursor.close()
		conexao.commit()
		print(f"{peca.nome} cadastrado com sucesso.")
	else:
		print("O item não é uma peça.")
def removerPeca(conexao, codPeca):
	cursor = conexao.cursor()
	cursor.execute("DELETE FROM estoque_pecas WHERE codPeca = codPeca")
	conexao.commit()
	print("removida com sucesso.")

def estoque_pecas(conexao):
	print("|Código |Descrição		  |Valor Unitário	|")
	cursor = conexao.cursor()
	comando_sql = "SELECT codPeca, descrição, valorUnitario FROM estoque_pecas"
	cursor.execute(comando_sql)
	#exibir na tela
	for (codPeca, descrição, valorUnitario) in cursor:
		print(f"|{codPeca}      |{descrição}            | {valorUnitario}			|")

	cursor.close()

def main():
	conexao = criar_conexao("localhost", "root", "root", "jcarteembarro")


	#testes
	p1 = Peca("Vasos", 10.00)

	#p2 = Peca("Potes", 50.00)
	#p1.alterarPreco(15)

	#cadastrarPeca(conexao, p1)

	#cadastrarPeca(p2)
	estoque_pecas(conexao)


	

	#print(p1)
	#v1 = Vendas(p1,"17/11/2021", 2)
	#v1.CalcularVenda()
	#print(v1)


main()