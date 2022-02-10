from model import *


def inserir(tabela, dados):
	tabela.insert_many(dados).execute()

#_________updates_____________________________

	
#_________consultas__________________________

def listar_dados_estoquePeca(): #consulta o banco de dados e retorna os dados da yabela estoque peças
	
	consulta = Peca.select().join(CategTamanho)
	
	tabela = []
	for peca in consulta:	
		tabela.append([peca.id, peca.nome, peca.valor_unit, peca.tamanhoPeca_id.tamanhoPeca, peca.qtd_estoque, peca.qtd_inicial, peca.qtd_entrada, peca.qtd_saida])
	
	return tabela

def listarDados_estoquePeca_porItem(condicao): #consulta o banco de dados e retorna os dados da yabela estoque peças
	consulta = Peca.select().join(CategTamanho).where(Peca.id == condicao)
	tabela = []
	for peca in consulta:	
		tabela.append([peca.id, peca.nome, peca.valor_unit, peca.tamanhoPeca_id.tamanhoPeca, peca.qtd_estoque, peca.qtd_inicial, peca.qtd_entrada, peca.qtd_saida])
	return tabela

def retornaTamanho(condicao):
	consulta = CategTamanho.select().where(CategTamanho.tamanhoPeca == condicao).get()
	return consulta

def retornaControleEntrada(condicao):
	consulta = Peca.select().join(Peca).where(ControleEntrada.peca_id == condicao)
	tabela = []
	for i in consulta:	
		tabela.append([i.id, i.peca_id.nome])
	return tabela	


'''def Login(login, senha):
	usuario_cadastrado = 'rafael'
	senha_cadastrada = '1234'
	if login == usuario_cadastrado and senha == senha_cadastrada:
		print('Acesso liberado.')
	elif login == usuario_cadastrado and senha != senha_cadastrada:
		print('Senha incorreta.')
	elif login != usuario_cadastrado and senha == senha_cadastrada:
		print('Usuário invalido')
	else:
		print('Usuário e senha incorretos.')'''