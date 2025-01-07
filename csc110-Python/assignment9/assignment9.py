# assignment9.py
#
# Student name: Naum Hoffman	
# Student id:  V00927502

tests = 0
passed = 0
import Song as s
import Playlist as p

def main():
	### PART 1: Song
	test_is_longer()
	test_count_with_artist()

	### Part 2: Playlist
	test_playlist_basics()
	test_are_equal()
	test_get_status()
	# test_next_song()

	print("TEST RESULTS:", passed, "/", tests)


########################
### PART 1 FUNCTIONS ###

def test_is_longer():
	print("testing is_longer")
	s1 = s.Song("Despacito", "Justin Bieber", 225)
	s2 = s.Song("Crazy", "Britney Spears", 245)
	s3 = s.Song("Champions", "Queen", 220)
	s4 = s.Song("The Motto", "Drake", 225)

	result = is_longer(s1, s2)
	print_test("testing with s1 and s2", result==s2)
	result = is_longer(s1, s3)
	print_test("testing with s1 and s3", result==s1)
	result = is_longer(s1, s4)
	print_test("testing with s1 and s4", result==s1)
	print()

# (Song, Song -> Song)
# return the song with the longest duration
def is_longer(s1, s2):
	if s1.get_duration() > s2.get_duration():
		return s1
	elif s1.get_duration() < s2.get_duration():
		return s2
	else:
		return s1

	



def test_count_with_artist():
	print("testing count_with_artist")
	s1 = s.Song("Despacito", "Justin Bieber", 225)
	s2 = s.Song("Crazy", "Britney Spears", 245)
	s3 = s.Song("Champions", "Queen", 220)
	s4 = s.Song("The Motto", "Drake", 225)
	s5 = s.Song("Baby", "Justin Bieber", 216)

	list0 = []
	result = count_with_artist(list0, "Justin Bieber")
	print_test("testing with empty and Bieber", result==0)

	list1 = [s1, s2, s3, s4, s5]
	result = count_with_artist(list1, "Elton John")
	print_test("testing with list1 and Elton John", result==0)
	result = count_with_artist(list1, "Drake")
	print_test("testing with list1 and Drake", result==1)
	result = count_with_artist(list1, "Justin Bieber")
	print_test("testing with list1 and Bieber", result==2)
	print()


# ((list of Song), str -> int)
# return a count of the number of songs
# in the list with the given artist
def count_with_artist(los, a):
	count = 0
	print(los)
	if los == []:
		return 0
	else:
		for q in los:
			print(q.get_artist())
			if q.get_artist() == a:
				count += 1
	return count 



def test_playlist_basics():
	print("testing playlist basics")
	list1 = []
	list2 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]

	list3 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]

	playlist1 = p.Playlist("None", list1)
	playlist2 = p.Playlist("Oldies", list2)
	playlist3 = p.Playlist("Top 40", list3)

	# Part a:
	print(playlist1) # what should be output here?
	# None (0)
	print(playlist2) # what should be output here?
	# Oldies (1265)
	print(playlist3) # what should be output here?
	#Top 40 (1326)
	# Part b:
	# TODO: add code here to update the name of playlist2 to "Classics"
	
	playlist2.set_name("Classics")
	print(playlist2) # This output should now be different
	#Classics (1265)

	# Part c:
	result = playlist1.get_duration()
	print_test("testing with playlist1", result == 0)
	# add a test for playlist2's duration
	result = playlist2.get_duration()
	print_test("testing with playlist2", result == 1265)
	# add a test for playlist3's duration
	result = playlist3.get_duration()
	print_test("testing with playlist3", result == 1326)


	#the value for the durations is added up within the playlist with calc duration

	# Part d:
	# add a song to a playlist and test that the playlist
	# has been updated appropriately (try adding songs
	# that already exist too). What attributes of a playlist
	# change when a song is added?

	new_playlist = playlist_basics(playlist1)
	result = new_playlist.get_duration()
	print_test("testing with list1", result == 120)

	print(list1)


def playlist_basics(a):
	new_song = s.Song("hello", "adele", 120)
	a.add_song(new_song)

	print(a)
	return a



def test_are_equal():
	print("testing are_equal")

	list1 = []
	list2 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]
	list3 = [s.Song("Africa", "Toto", 295), \
			 s.Song("Champions", "Queen", 220), \
			 s.Song("Like a Prayer", "Madonna", 319), \
			 s.Song("Hey Jude", "The Beatles", 431)]
	list4 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas 	Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]

	playlist1 = p.Playlist("None", list1)
	playlist2 = p.Playlist("Oldies", list2)
	playlist3 = p.Playlist("Favs", list3)
	playlist4 = p.Playlist("Top 40", list4)

	isTrue = are_equal(playlist2, playlist3)
	result = isTrue
	print_test("testing with playlist2 and 3", result == True)

	isTrue = are_equal(playlist1, playlist3)
	result = isTrue
	print_test("testing with playlist 1 and 3", result == False)

	isTrue = are_equal(playlist2, playlist4)
	result = isTrue
	print_test("testing with playlist 2 and 4", result == False)


	# TODO: Add tests to determine if two
	# playlists are equal.

def are_equal(p1, p2):
	if p1 == p2:
		return True
	else:
		return False


def test_get_status():
	
	list1 = []
	list2 = [s.Song("Champions", "Queen", 220), \
			 s.Song("Africa", "Toto", 295), \
			 s.Song("Hey Jude", "The Beatles", 431), \
			 s.Song("Like a Prayer", "Madonna", 319)]
	list3 = [s.Song("Africa", "Toto", 295), \
			 s.Song("Champions", "Queen", 220), \
			 s.Song("Like a Prayer", "Madonna", 319), \
			 s.Song("Hey Jude", "The Beatles", 431)]
	list4 = [s.Song("Someone You Loved", "Lewis Capaldi", 182), \
			 s.Song("Circles", "Post Malone", 215), \
			 s.Song("Truth Hurts", "Lizzo", 173), \
			 s.Song("Only Human", "Jonas 	Brothers", 183), \
			 s.Song("Senorita", "Shawn Mendes", 191), \
			 s.Song("Beautiful People", "Ed Sheeren", 207), \
			 s.Song("Goodbyes", "Post Malone", 175)]

	playlist1 = p.Playlist("None", list1)
	playlist2 = p.Playlist("Oldies", list2)
	playlist3 = p.Playlist("Favs", list3)
	playlist4 = p.Playlist("Top 40", list4)

	print("Testing get_status")
	isTrue = playlist2.get_status(20)
	print(isTrue)
	result = isTrue
	print_test("testing with 20 sec", result)



	# TODO: Add tests to test the get_status
	# method found in the Playlist.py class
	

	#print(playlist.get_songs())
	#print(playlist.get_duration())
	





def test_next_song():
	print("Testing next_song")
	# TODO: Add tests to test the next_song()
	# method found in the Playlist.py class

#def next_song():




# (str, bool -> None)
# takes the name or description of a test and whether the
# test produced the expected output (True) or not (False)
# and prints out whether that test passed or failed
# NOTE: You should not have to modify this in any way.
def print_test(test_name, result_correct):
	global tests
	global passed
	tests += 1
	if(result_correct):
		print(test_name + ": passed")
		passed += 1
	else:
		print(test_name + ": failed")

# The following code will call your main function
if __name__ == '__main__':
	main()
