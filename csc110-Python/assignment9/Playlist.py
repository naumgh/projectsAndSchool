class Playlist:
	# (str, str, (list of Song) -> None)
	# constructor for the Playlist class
	def __init__(self, name, songs):
		self.name = name
		self.songs = songs
		self.duration = self.calc_duration()

	# (None -> str)
	# return a string with the name and duration of the playlist
	def __str__(self):
		return self.name + " (" + str(self.duration) + ")"

	# (None -> str)
	# return a string with the name of the playlist
	def __repr__(self):
		return self.name

	# (Playlist -> bool)
	# return True if the other playlist contains
	# all of the exact same songs, False otherwise
	def __eq__(self, other):
		if self.name == other.get_name():
			return True
		else:
			return False

	# (None -> str)
	# return name of the playlist
	def get_name(self):
		return self.name

	# (str -> None)
	# update the name of the playlist to new_name
	def set_name(self, new_name):
		self.name = new_name

	# (None -> (list of Song))
	# return the list of songs in the playlist
	def get_songs(self):
		return self.songs

	# ((list of Song)) -> None)
	# change the list of songs in the playlist to the given list
	def set_songs(self, song_list):
		self.songs = song_list
		self.duration = calc_duration()

	# (None -> int)
	# return the duration of the playlist
	def get_duration(self):
		return self.duration

	# (None -> int)
	# return the sum of all song durations
	def calc_duration(self):
		sum = 0
		for s in self.songs:
			sum += s.get_duration()
		return sum

	# (Song -> None)
	# add new_song to the songs list if it is not already in the playlist
	def add_song(self, new_song):
		if new_song not in self.songs:
			self.songs.append(new_song)
			self.duration = self.calc_duration()

	# (Song -> None)
	# remove a song from the songs list
	def remove_song(self, song):
		if song in self.songs:
			self.songs.remove(song)
		self.duration = self.calc_duration()


	# (int -> tuple)
	# given an amount of time the playlist has been
	# playing, return a tuple of the form (str, int)
	# containing the name of the current song, and
	# how many seconds the song has been playing
	def get_status(self, current):
		time = current
		playlist = self.get_songs()

		if time >= 0:
			song = playlist.pop(0)
			time = time - song.get_duration()
		else:
			return song, 0

		return song, 0 - time

	# (Song -> Song)
	# given a song, return the next song in the playlist
	# Assume the given song is in the playlist
	'''
	def next_song(self, title):
		list = self.get_songs():
		for i in list:
			print(i)

	'''