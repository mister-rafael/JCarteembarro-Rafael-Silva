#BIBLIOTECAS
import PySimpleGUI as sg #RECURSO GRÁFICO
from model import *
from crud import *

class CadastroMaterial:
	def __init__(self):
		#layout
		layout2 = [
				[sg.Text('Material', size = (20,0)), sg.Input(size = (20,0), key = 'nome_material')],
				[sg.Text('Unidade de Medida', size = (20,0)), sg.Input(size = (20,0), key = 'unid_medida')],
				[sg.Text('Quantidade atual', size = (20,0)), sg.Input(size = (20,0), key = 'qtd_estoque_m')],
				[sg.Text('Quantidade inicial', size = (20,0)), sg.Input(size = (20,0), key = 'qtd_inicial_m')],
				[sg.Text('Quantidade de entrada', size = (20,0)), sg.Input(size = (20,0), key = 'qtd_entrada_m')],
				[sg.Text('Quantidade de saída', size = (20,0)), sg.Input(size = (20,0), key = 'qtd_saida_m')],
				[sg.Text('Data da ultima compra', size = (20,0)), sg.Input(size = (20,0), key = 'ultima_compra')],
				[sg.Output(size = (50,10))],	
				[sg.Button('Cadastrar material')]
		]
		#Janelas
		self.janela2 = sg.Window('Cadastro de materiais').layout(layout2)

	def Iniciar(self):
		while True:
			#Extrair dados, ou manipulação de eventos
			self.button, self.values = self.janela2.Read()
			materiais = [{	#inicio da lista que guarda os valores obtidos do formulário
						'nome': self.values['nome_material'],
						'und_medida':self.values['unid_medida'],  
						'qtd_estoque':self.values['qtd_estoque_m'], 
						'qtd_inicial':self.values['qtd_inicial_m'], 
						'qtd_entrada':self.values['qtd_entrada_m'], 
						'qtd_saida':self.values['qtd_saida_m'],
						'ultima_compra':self.values['ultima_compra']
					}]#fim da lista
			inserir(materiais, Material)#função que insere uma quantidade maior de dados.
			print(f'''
					Nome: {self.values['nome_material']}
					Unidade de medida:{self.values['unid_medida']}
					Qtd_estoque:{self.values['qtd_estoque_m']}
					Qtd_inicial:{self.values['qtd_inicial_m']} 
					Qtd_entrada:{self.values['qtd_entrada_m']}
					Qtd_saida:{self.values['qtd_saida_m']}
					Data da ultima compra:{self.values['ultima_compra']}''')