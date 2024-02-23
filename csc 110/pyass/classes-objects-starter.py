
import Song as s

# Create a Song class in a Song.py file
# Q1. create a Song object with your choice of data
song1 = s.Song("Despacito", 225, "justin beiber")


# Q2. print out the title of your song object
print(song1.get_title())

# Q3. update the duration of your song and then print it out
print(song1.get_duration())
song1.set_duration(180)
#todo
print(song1.get_duration())

# Q4. create another 2 song objects with your choice of data
song2 = s.Song("crazy","britney spears",245)
song3 = s.Song("champions", "queen", 220)

# Q5. create a list of your 3 songs
list1 = [song1, song2, song3]

print(list1)

print(song1)
# Q6. loop through your list of songs and print out all of the titles
for s in list1:
	print(s.get_title())

# Q7. write and test a function that takes list of Songs
#     and returns the total length of all the songs
for r in list1:
	print(r.get_duration())

