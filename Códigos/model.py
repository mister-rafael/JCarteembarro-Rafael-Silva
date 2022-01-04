from datetime import datetime
from peewee import ( SqliteDatabase, Model, TextField, ForeignKeyField,DateTimeField, IntegerField, DecimalField)

db = SqliteDatabase('bancoDeDados_jc.db') #DATABASE (BANCO DE DADOS)

class BaseModel(Model):
	class Meta:
		database = db

#PARTE DE PEÇAS
class CategTamanho(BaseModel):
	tamanhoPeca = TextField(unique = True) #Informa se a peça é (principalmente, quando for conjunto): PEQUENA, MÉDIA, GRANDE ou tamanho UNICO


class Peca(BaseModel): #Peça seria o produto que é comercializado. E pode-se vender mais de uma peça por vez, mas, uma peça só pode ser vendida uma vez.
	nome = TextField()
	valor_unit = DecimalField()
	tamanhoPeca = ForeignKeyField(CategTamanho, backref='pecas') #recebe chave estrangeira
	qtd_estoque = IntegerField()
	qtd_inicial = IntegerField()
	qtd_entrada = IntegerField()
	qtd_saida = IntegerField()


class ItemVenda(BaseModel): #Pode-se vender mais de uma peça por vez, mas, uma peça só pode ser vendida uma vez.
	peca = ForeignKeyField(Peca, backref='item_venda') #recebe chave estrangeira #chave estrangeira
	dataVenda = DateTimeField(default=datetime.now)
	qtd_vendida = IntegerField()
	desconto = DecimalField()
	total = DecimalField()


class ControleEntrada(BaseModel):
	peca = ForeignKeyField(Peca, backref='controle_entrada') #recebe chave estrangeira #chave estrangeira
	dataEntrada = DateTimeField(default=datetime.now)
	qtd_entrada = IntegerField()
'''try:
	db.create_tables([Peca, CategTamanho, ItemVenda, ControleEntrada])
	print("Tabela criadas com sucesso")
except:
	print("Tabela já existem no banco.")'''

#PARTE DE MATERIAIS

class Material(BaseModel):
	nome	= TextField()
	und_medida = TextField()
	qtd_estoque = IntegerField()
	qtd_inicial = IntegerField()
	qtd_entrada = IntegerField()
	qtd_saida = IntegerField()
	ultima_compra = DateTimeField()

class ControleSaida(BaseModel):
	produto = ForeignKeyField(Material, backref = 'controleSaida') #chave estrangeira para a tabela Material
	dataSaida = DateTimeField(default = datetime.now)
	quantidade = IntegerField()

class ItemCompra(BaseModel):
	produto = ForeignKeyField(Material, backref = 'item_entrada') #chave estrangeira para a tabela Material
	dataCompra = DateTimeField(default = datetime.now)
	qtd_comprada = IntegerField()
	valor_unit = DecimalField()
	desconto = DecimalField()
	valor_pago = DecimalField()


try:
	db.create_tables([Material, ControleSaida , ItemCompra])
	print("Tabela criadas com sucesso")
except:
	print("Tabela já existem no banco.")