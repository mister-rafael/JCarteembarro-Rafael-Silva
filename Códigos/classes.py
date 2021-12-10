from datetime import datetime
from peewee import ( SqliteDatabase, Model, TextField, ForeignKeyField,DateTimeField, IntegerField)

base_dados = SqliteDatabase('bancoDeDados_jc.db')

class BaseModel(Model):
	class Meta:
		database = base_dados


class Peca(BaseModel): #Peça seria o produto que é comercializado. E pode-se vender mais de uma peça por vez, mas, uma peça só pode ser vendida uma vez.
	nome = ...
	valor_unit = ...
	tamanhoPeca = ... #recebe chave estrangeira
	qtd_estoque = ...
	saldo_inicial = ...
	qtd_entrada = ...
	qtd_saida = ...


	def __init__(self, nome, valor_unit):
		self.__nome = nome
		self.__valor_unit = valor_unit

	def __str__(self):
		return f"|{self.__nome}.					|R${self.__valor_unit}			|"

	@property
	def nome(self):
		return self.__nome
	
	@property
	def valor(self):
		return self.__valor_unit

	@valor.setter
	def valor(self, valor):
		self.__valor_unit = valor_unit
	#Métodos
	def alterarPreco(self, novo_valor): #este metodo permite que após cadastrado uma peça, esta possa ter o valor alterado.
		self.__valor_unit = novo_valor
		print("Valor alterado.")

class item_Venda(BaseModel): #Pode-se vender mais de uma peça por vez, mas, uma peça só pode ser vendida uma vez.
	def __init__(self, peca, data, quantidade, forma_pag, desconto=0):
		if type(peca) == Peca:
			self.__peca = peca
		else:
			self.__peca = None
		self.__data = data
		self.__quantidade = quantidade
		self.__forma_pag = forma_pag
		self.__desconto = desconto
		self.__valorAPagar = 0

	def __str__(self):
		return f"Produto vendido: {self.__peca}"

class controle_entrada:
	peca = ...
	dataEntrada = ...
	qtd_entrada = ...

class categTamanho:
	pass





