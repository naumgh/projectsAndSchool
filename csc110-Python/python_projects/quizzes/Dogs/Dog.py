class Dog:
	#compiler

	def __init__(self, name, species, vaccines):
		self.name = name
		self.species = species
		self.vaccines = vaccines

	def __str__(self):
		return self.name  + ' ' + self.species


	def __repr__(self):
		return self.name

	def __eq__(self, other):
		if self.name == other.get_name():
			return True
		else:
			return False

	def get_species(self):
		return self.species

	def set_species(self, species):
		self.species = species

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_vaccines(self):
		return self.vaccines

	def set_vaccines(self, vaccines):
		self.vaccines = vaccines

def main():
	d1 = Dog("pug", "polly", "[H1Z1, SQINE FLU, RABIES]")
	d2 = Dog("mastiff", "alexi", "'none")

	print(d1)
	print(d2)

	dogs = [d1, d2]
	print(dogs)