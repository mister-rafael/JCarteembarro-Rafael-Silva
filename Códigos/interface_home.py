#BIBLIOTECAS
import PySimpleGUI as sg #RECURSO GRÁFICO
from model import *
from crud import *

#CLASSES
#janela 1
def Home():
	layout = [[sg.Text('Vendas'), sg.Text('Despezas')],[sg.Button('Continuar')]]

	return sg.Window('Home', layout = layout, finalize = True)

def Venda():
	layout = [
			[sg.Text('Data da venda'), sg.Input(key = 'dataVenda')], 
			[sg.Text('Produto'), sg.Input(key = 'peca_id')],
			[sg.Text('Quantidade'), sg.Input(key = 'qtd_vendida')],
			[sg.Text('Desconto'), sg.Input(key = 'desconto')],
			[sg.Text('Total a pagar'), sg.Input(key = 'total')],
			[sg.Button('Voltar')]
			]

	return sg.Window('Vendas', layout = layout, finalize = True)
		
janela1, janela2 = Home(), None

while True:
	window,event,values = sg.read_all_windows()

	#quando a janela for fechada:
	if window == janela1 and event == sg.WIN_CLOSED:
		break
	#quando queremos ir para a proxima janela
	if window == janela1 and event == 'Continuar':
		janela2 = Venda()
		janela1.hide()
	#quando queremos voltar para a janela anterior	
	if window == janela2 and event == 'Voltar':
		janela2.hide()
		janela1.un_hide()
