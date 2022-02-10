from model import *
from crud import *


def CalcularEstoque(qtd_inicial, qtd_entrada, qtd_saida):
	estoqueAtual = (qtd_inicial + qtd_entrada)-qtd_saida
	return estoqueAtual

def atualizarQtdEstoquePeca(criterio):
    #db.connect()
    consulta = Peca.select().where(Peca.id == criterio).get()
    estoqueAtual = CalcularEstoque(consulta.qtd_inicial, consulta.qtd_entrada, consulta.qtd_saida)
    Peca.update(qtd_estoque = estoqueAtual).where(Peca.id == criterio).execute()
    db.close()
    return estoqueAtual

def atualizarQtdEntradaPeca(criterio, valor):
    #db.connect()
    consulta = Peca.select().where(Peca.id == criterio).get()
    quant_nova = int(consulta.qtd_entrada) + int(valor) #quantidade anterior + o novo valor de entrada
    Peca.update(qtd_entrada = quant_nova).where(Peca.id == criterio).execute()
    db.close()
    return quant_nova