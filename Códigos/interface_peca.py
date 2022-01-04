#BIBLIOTECAS
import PySimpleGUI as sg #RECURSO GRÁFICO
from model import *
from crud import *

#CLASSES
class CadastroPeca:
	def __init__(self):
		#layout
		layout = [
				[sg.Text('Peça', size = (15,0)), sg.Input(size = (15,0), key = 'nome')],
				[sg.Text('Valor Unitário', size = (15,0)), sg.Input(size = (15,0), key = 'valor_unit')],
				[sg.Text('Tamanho', size = (15,0)), sg.Input(size = (15,0), key = 'tamanhoPeca')],
				[sg.Text('Quantidade atual', size = (15,0)), sg.Input(size = (15,0), key = 'qtd_estoque')],
				[sg.Text('Quantidade inicial', size = (15,0)), sg.Input(size = (15,0), key = 'qtd_inicial')],
				[sg.Text('Quantidade de entrada', size = (15,0)), sg.Input(size = (15,0), key = 'qtd_entrada')],
				[sg.Text('Quantidade de saída', size = (15,0)), sg.Input(size = (15,0), key = 'qtd_saida')],
				[sg.Output(size = (30,20))],	
				[sg.Button('Cadastrar peça')]
		]
		#Janelas
		self.janela = sg.Window('Cadastro de peças').layout(layout)

	def Iniciar(self):
		while True:
			#Extrair dados, ou manipulação de eventos
			self.button, self.values = self.janela.Read()
			pecas = [{	#inicio da lista que guarda os valores obtidos do formulário
						'nome': self.values['nome'],
						'valor_unit':self.values['valor_unit'], 
						'tamanhoPeca_id':self.values['tamanhoPeca'], 
						'qtd_estoque':self.values['qtd_estoque'], 
						'qtd_inicial':self.values['qtd_inicial'], 
						'qtd_entrada':self.values['qtd_entrada'], 
						'qtd_saida':self.values['qtd_saida'] 
					}]#fim da lista
			inserir(pecas, Peca)#função que insere uma quantidade maior de dados.
			if inserir(pecas, Peca) == True:
				print(f'''
						Nome: {self.values['nome']}
						Valor Initário:{self.values['valor_unit']}
						Tamanho da peça:{self.values['tamanhoPeca']} 
						Qtd_estoque:{self.values['qtd_estoque']}
						Qtd_inicial:{self.values['qtd_inicial']} 
						Qtd_entrada:{self.values['qtd_entrada']}
						Qtd_saida:{self.values['qtd_saida']}''')
			
			else:
				print("Há dados repetidos")


			
			