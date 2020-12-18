from time import gmtime, strftime


class Soda:

	def name(self):
		raise ValueError()

	def sweetener(self):
		raise ValueError()

	def colourant(self):
		raise ValueError()

	def __repr__(self):
		return f'{self.name()} {self.sweetener()} {self.colourant()}'


class Pepsi(Soda):

	def name(self):
		return 'Pepsi'

	def sweetener(self):
		return 'sugar'

	def colourant(self):
		return 'black'


class ColaLight(Soda):

	def name(self):
		return 'Coca-Cola Light'

	def sweetener(self):
		return 'sucralose'

	def colourant(self):
		return 'brown'


class SodaFactory:

	def create(self):
		raise ValueError()


class PepsiCo(SodaFactory):

	def create(self):
		return Pepsi()


class CocaCola(SodaFactory):

	def create(self):
		return ColaLight()


class Journal:

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Journal, cls).__new__(cls)
			cls.instance.records = []
		return cls.instance

	def add_record(self, soda, count):
		data = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		rec = JournalEntry(soda, count, data)
		self.records.append(rec)

	def __repr__(self):
		return '\n'.join(map(str, self.records))


class JournalEntry:

	def __init__(self, soda, count, data):
		self.soda = soda
		self.count = count
		self.data = data

	def __repr__(self):
		return f'{self.soda}; {self.count} шт.; {self.data}'


while True:
	_input = input('Введите название фабрики и количество бутылок: ')
	if _input == '':
		break
	factory, bottles_count = _input.split()
	if factory == 'PepsiCo':
		_soda = PepsiCo()
	elif factory == 'Coca-Cola':
		_soda = CocaCola()
	else:
		print('Такой фабрики не существует. Пожалуйста, введите название фабрики и количество бутылок еще раз')
		continue
	journal = Journal()
	journal.add_record(_soda.create(), int(bottles_count))
	print(journal)
