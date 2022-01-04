from model import *
from crud import *
from interface_peca import (CadastroPeca)
from interface_material import (CadastroMaterial)
#ADCIONAR DADOS EM:

#PEÇA
pecas = [
	{'nome': 'Vasos','valor_unit':'10', 'tamanhoPeca':'4', 'qtd_estoque':'10', 'qtd_inicial':'0', 'qtd_entrada':'1', 'qtd_saida':'1' },
	{'nome': 'Conjunto de garrafas','valor_unit':'35', 'tamanhoPeca':'2', 'qtd_estoque':'5', 'qtd_inicial':'0', 'qtd_entrada':'1', 'qtd_saida':'1' },
	{'nome': 'Coruja','valor_unit':'25', 'tamanhoPeca':'2', 'qtd_estoque':'10', 'qtd_inicial':'0', 'qtd_entrada':'1', 'qtd_saida':'1' },
]
#CATEGORIA
categorias = [
	{'tamanhoPeca': 'Pequeno'},
	{'tamanhoPeca': 'Médio'},
	{'tamanhoPeca': 'Grande'},
	{'tamanhoPeca': 'Unico'},
]
#ITEM VENDA
vendas = [
	{'peca': '1','dataVenda':'09/12/2021', 'qtd_vendida':'1', 'desconto':'2', 'total':'8'},
	{'peca': '2','dataVenda':'09/12/2021', 'qtd_vendida':'1', 'desconto':'2', 'total':'18'},
	{'peca': '3','dataVenda':'09/12/2021', 'qtd_vendida':'1', 'desconto':'2', 'total':'23'},
]
#CONTROLE ENTRADA
entradas = [
	{'peca': '3','dataEntrada':'01/12/2021', 'qtd_entrada':'8'},
	{'peca': '3','dataEntrada':'01/12/2021', 'qtd_entrada':'8'},
	{'peca': '3','dataEntrada':'01/12/2021', 'qtd_entrada':'8'},
]
materiais = [
	{'nome': 'Massa corrida','und_medida':'Lata', 'qtd_estoque':'10', 'qtd_inicial':'0', 'qtd_entrada':'1', 'qtd_saida':'1', 'ultima_compra':'02/03/2021'},
	{'nome': 'Tinta','und_medida':'Unidade', 'qtd_estoque':'10', 'qtd_inicial':'0', 'qtd_entrada':'1', 'qtd_saida':'1', 'ultima_compra':'02/04/2021'},
	{'nome': 'Lixa','und_medida':'Unidade', 'qtd_estoque':'10', 'qtd_inicial':'0', 'qtd_entrada':'1', 'qtd_saida':'1', 'ultima_compra':'02/05/2021'},
]

#inserir(CategTamanho, categorias) #chamando um CRUD
#inserir(pecas, Peca) #chamando um CRUD
#inserir(ControleEntrada, entradas) #chamando um CRUD
#inserir(ItemVenda, vendas) #chamando um CRUD
#inserir(materiais, Material)
#consultar(ItemVenda)

'''resultado = Peca.select(Peca.nome).join(ItemVenda)
for i in resultado:
	print(i)'''


#tela = CadastroPeca()

#tela.Iniciar()

tela2 = CadastroMaterial()
tela2.Iniciar()