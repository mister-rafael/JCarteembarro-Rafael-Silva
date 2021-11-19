#CLASSE PEÇA
class Peca: #Peça seria o produto que é comercializado. E pode-se vender mais de uma peça por vez, mas, uma peça só pode ser vendida uma vez.
	def __init__(self, codigo, nome, valor_unit):
		self.__codigo = codigo
		self.__nome = nome
		self.__valor_unit = valor_unit

	def __str__(self):
		return f"|{self.__codigo}			|{self.__nome}.					|R${self.__valor_unit}			|"

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

#CLASSE VENDA
class Venda(Peca): #Pode-se vender mais de uma peça por vez, mas, uma peça só pode ser vendida uma vez.
	seq_pin = 0
	def __init__(self, peca, data, quantidade, forma_pag, desconto=0):
		Venda.seq_pin += 1 #atribui um id de venda, que é unico.
		self.__id_venda = Venda.seq_pin
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



