# Song.py for CSC 110 Fall 2019 semester
# This file must not be changed in any way
# when working through Assignment 9
class Song:
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		self.duration = duration

	def __str__(self):
		result = '"' + self.title + '" - ' + self.artist
		return result

	def __repr__(self):
		return self.title

	def __eq__(self, other):
		if (type(other) != Song):
			return False
		if self.title == other.get_title() and self.artist == other.get_artist():
			return True
		else:
			return False

	def get_title(self):
		return self.title

	def set_title(self, title):
		self.title = title

	def get_artist(self):
		return self.artist

	def set_artist(self, artist):
		self.artist = artist

	def get_duration(self):
		return self.duration

	def set_duration(self, duration):
		self.duration = duration
