class Song:
	def __init__(self, title, duration, artist):
		self.title = title
		self.duration = duration
		self.artist = artist
	
	def __str__(self):
		result = "song: " + self.title
		return result

	def __repr__(self):
		return self.title

	def __eq__(self, other):
		if self.title == other.get_title() and self.artist == other.get_artist():
			return True
		else:
			return False

	def get_artist(self):
		return self.artist
	def get_title(self):
		return self.title
	def get_duration(self):
		return self.duration
	def set_duration(self, new_duration):
		song1 = new_duration
