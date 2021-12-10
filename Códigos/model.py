from datetime import datetime
from peewee import ( SqliteDatabase, Model, TextField, ForeignKeyField,DateTimeField, IntegerField, DecimalField)

db = SqliteDatabase('bancoDeDados_jc.db') #DATABASE (BANCO DE DADOS)

class BaseModel(Model):
	class Meta:
		database = db

class CategTamanho(BaseModel):
	tamanhoPeca = TextField() #Informa se a peça é (principalemente, quando for conjunto): PEQUENA, MÉDIA, GRANDE ou tamanho UNICO


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

db.create_tables([Peca, CategTamanho, ItemVenda, ControleEntrada])