def main():
	
	outer_inner_loop()
	#escape()
	#operations_and_their_orders()
	#foramtting_strings()
	#sets()
	#lists()
	dictionaries()
	#bubble_sort()
	#selection_sort()
	#test(5)
	x = 9
	y = 2
	z = 5
	#param(z, y, x)
	#param(y, x, x)



def selection_sort():
	A = [0, 7, 3, 21, 1, 100] 

# Traverse through all array elements 
	for i in range(len(A)): 
	# Find the minimum element in remaining  
	# unsorted array 
		min_idx = i 
		for j in range(i+1, len(A)): 
			if A[min_idx] > A[j]: 
				min_idx = j 
	# Swap the found minimum element with  
	# the first element         
		A[i], A[min_idx] = A[min_idx], A[i] 

#Driver code to test above 
		print(A)


def bubble_sort():
	list1 = [0, 7, 3, 21, 1, 100]
	n = len(list1)
	for i in range(n):
		for val in range(n-1):
			if list1[val] > list1[val+1]:
				list1[val], list1[val+1] = list1[val+1], list1[val]
				'''
				mike_sherm = list1[val]
				list1[val]= list1[val+1]
				list1[val+1] = mike_sherm
				'''
				print(list1)
	print("")
	




def test(x):
	for x in range(1, x+1):
		print(x**2)


def param(x,z,y):
	print(z, (y-x))
	
def lists():
	#list splicing
	nums = [7, 1, 4, 3, 5, 9]
	new_list = nums[2:6]
	print(new_list)
	new_list = nums[1:-1]
	print(new_list)
	new_list = nums[2:6:2]
	print(new_list)
	new_list = nums[:3:-1]
	print(new_list)
	#lists of lists
	values = [[0, 5, 3], [9, 8, 1], [6, 6, 6]]
	print(values[0])
	print(values[1][2])


def sets():
	a = set(["john", "amy", "yiyi", "ali", "deep", "sam"])
	b = set(["yiyi", "taya", "cam", "ali"])
	#union of sets:
	c = a.union(b)
	print(c)
	#intersection of sets:
	d = a.intersection(b)
	print(d)
	#difference of sets:
	e = a - b 
	print(e)
	f = b - a
	print(f)



def outer_inner_loop():
	for row in range(1,5):
		for col in range(row):
			print(col,end='')
		print("!")
	


def escape():
	print("my name is \nnaum")
	print("shut the fuck up\tfaggot")
	print("who the fuck you calling faggot \"retard\"")
	print("HEY DONT CALL ME \\THAT >:C")


#types of operations and their orders----------
def operations_and_their_orders():
	print("the order goes: exopnonets, parenthesis|multiplication, division, intiger division, modulus|, subtraction, addition")
	print(10 + 2)
	print(10-2)
	print(10 * 2)
	print(10/2)
	print(23//2)
	print(23%2)
	print(2**3)
	print(2**3 + 4%2 - (3//2)/2)




#-----------

#formatting strings and floats---------
def foramtting_strings():
	a = 6/2
	print("Hello!","\this is \\ \'my// name %8.5f"%a)

	print("hello", "world", sep = '!')
	print("hello")

	print("hello world", end = '!')
	print("hello")

	print(format(12345.6789, ".2f"))
	print(format(12345.6789, ".3f"))

#----------


#dictionaries---------

def dictionaries():
	#creating a dictionary
	dict_songs = {"ps & qs":("little uzi vert", 243), 
					"FN": ("lil Tjay", 330),
					"molly":("ian dior", 256),
					"aint doin that": ("playboy cardi", 253)}
	'''
	print(dict_songs)
	#return dict_songs
	#accessing entries in a dictionary
	

	for x in dict_songs:
		print(x, dict_songs[x])

	for key, value in dict_songs.items():
		print(key, value)
	'''
	for key, value in dict_songs.items():
		artist_name = value[0] 
		print(artist_name)
	#adding, overwriting, and deleting keys and values in a dictionary
	#keys are immutable
	
	'''
	dict_songs['reply'] = ("trippie redd", 257)
	print(dict_songs)
	print(" ")
	dict_songs['reply'] = ("aboogy /w a hoodie", 304)
	print(dict_songs)
	print(" ")
	del dict_songs['FN']
	print(dict_songs)
	print(" ")

	#getting the number of elements in a dictionary
	dict_length = len(dict_songs)
	print(dict_length)
	#you can even mix different values withen a dictionary
	dict_songs[450] = ('Oasis', 'Don''t look back in anger')
	dict_songs[10101] = (1110010010010, 1010010011)
	print(" ")
	print(dict_songs)
	print(" ")
	#some important dictionary methods:
	#clear - clears the contents of a dictionary
	new_dict = dict(dict_songs)
	new_dict.clear()
	print(new_dict)
	print(" ")
	
	#get - gets the value associated with a specified key. if the key is not found , the 
	#method does not raise an exception. instead, it returns a default value
	value = dict_songs.get('molly', 'key not found')


	#items - returns all the keys in a dictionary and their associated values as a 
	#sequence of tuples. (refrenced above)
	all_items = dict_songs.items()
	print(all_items)
	print(" ")
	
	#keys - returns all the keys in a dictionary as a sequence of tuples
	all_keys = dict_songs.keys()
	print(all_keys)
	print(" ")

	#pop- returns the value associated with a specified key and removes that key-value
	#pair from the dicitonary. if the key is not found, the method returns a default value.
	poppers = dict_songs.pop(450, "key not found")
	print(poppers)
	#popitem - same shit but its random
	k, v = dict_songs.popitem()
	print(k, v)
	#values - returns all the values in the dictionary as a sequence of tuples
	all_values = dict_songs.values()
	print(" ")
	print(all_values)
	'''


#writing some actual programs(to do on later notice):


#-------------------






if __name__ == '__main__':
	main()
