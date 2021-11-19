from classes import *
pecas = []
vendas = []

def cadastrarPeca(peca):
	if isinstance(peca, Peca):
		pecas.append(peca)
		print(f"{peca.nome} cadastrado com sucesso.")
	else:
		print("O item não é uma peça.")

def estoque_pecas():
	print("|Código			|Descrição				|Valor Unitário	|")
	for peca in pecas:
		print(peca)

def main():
	p1 = Peca("P_1", "Vasos", 10.00)
	p2 = Peca("P_2", "Potes", 50.00)
	p1.alterarPreco(15)
	
	cadastrarPeca(p1)
	cadastrarPeca(p2)

	estoque_pecas()


	

	#print(p1)

	#v1 = Vendas(p1,"17/11/2021", 2)


	#v1.CalcularVenda()

	#print(v1)
main()