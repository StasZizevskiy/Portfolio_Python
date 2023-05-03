class Purse:
	def __init__(self, valuta, name = 'Unknown'):
		if valuta not in ('USD', 'EUR'):
			raise ValueError ('Только USD, EUR')
		self.__money = 0.00
		self.valuta = valuta
		self.name = name
		print('кошелёк создан')

	def top_up_balance(self, howmany):
		self.__money = self.__money + howmany
		print('Кошелёк пополнен на ' + str(howmany) + self.valuta)
		return howmany

	def top_down_balance(self, howmany):
		if self.__money - howmany < 0:
			raise ValueError ('Недостаточно средств')
		self.__money = self.__money - howmany
		print('С кошелька снято ' + str(howmany) + self.valuta)
		return howmany

	def info(self):
		print(self.__money)

	def __del__(self):
		print('Кошелёк удалён')
		


