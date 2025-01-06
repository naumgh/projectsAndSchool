class Teams:

	def __init__(self, years, names):
		self.names = names 
		self.years = years


	def __str__(self):
		return self.names+" "+self.years

	def __repr__(self):
		return self.names+":"+ str(self.years)

	def get_years(self):
		return self.years