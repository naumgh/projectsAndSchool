# assignment8.py
#
# Student name: Naum Hoffman
# Student id:  V00927502

tests = 0
passed = 0
THRESHOLD = 0.1

def main():
	# PART 1: Dictionary Functions
	test_get_value()
	test_sum_values()
	test_frequency_percentage()

	# Part 2: Creating a Dictionary from an input file
	test_frequency_dictionary()

	# Part 3: Converting to list of tuples and sorting
	test_dict_to_list()
	test_swap()
	test_find_max_index_from()
	test_selection_sort()

	# Part 4: Statistics
	test_write_most_frequent()

	print("TEST RESULTS:", passed, "/", tests)


########################
### PART 1 FUNCTIONS ###

def test_get_value():
	print("testing get_value")
	dict0 = {}
	result = get_value(dict0, "a")
	print_test("testing with empty dictionary and a", result==0)

	dict1 = {"a":4, "bc":2, "defg":1, "hi":3}
	result = get_value(dict1, "z")
	print_test("testing with dict1 and z", result==0)
	result = get_value(dict1, "hi")
	print_test("testing with dict1 and hi", result==3)
	result = get_value(dict1, "bc")
	print_test("testing with dict1 and bc", result==2)

	dict2 = {"computer":110, "science":99}
	result = get_value(dict2, "hi")
	print_test("testing with dict2 and hi", result==0)
	result = get_value(dict2, "computer")
	print_test("testing with dict2 and computer", result==110)
	print()

def test_sum_values():
	print("testing sum_values")
	dict0 = {}
	dict1 = {"a":4, "bc":2, "defg":1, "hi":3}
	dict2 = {"computer":110, "science":99}
	result = sum_values(dict0)
	print_test("testing with empty dictionary", result==0)
	result = sum_values(dict1)
	print_test("testing with dict1", result==4+2+1+3)
	result = sum_values(dict2)
	print_test("testing with dict2", result==110+99)
	print()

def test_frequency_percentage():
	print ("testing frequeny_percentage")
	dict0 = {}
	result = frequency_percentage(dict0, "a")
	print_test("testing with empty dictionary and a", abs(result-0)<THRESHOLD)

	dict1 = {"a":4, "bc":2, "defg":1, "hi":3}
	result = frequency_percentage(dict1, "hi")
	expected = 3 / (4 + 2 + 1 + 3)
	print_test("testing with dict1 and hi", abs(result-expected)<THRESHOLD)
	result = frequency_percentage(dict1, "a")
	expected = 4 / (4 + 2 + 1 + 3)
	print_test("testing with dict1 and a", abs(result-expected)<THRESHOLD)

	dict2 = {"computer":110, "science":99}
	result = frequency_percentage(dict2, "science")
	expected = 99 / (110 + 99)
	print_test("testing with dict2 and science", abs(result-expected)<THRESHOLD)
	print()

# (dict, str -> int)
# return the value for the dictionary item with the given key or 0
# if the dictionary does not contain an item with the given key
# the form of the given dictionary is {str: int}
def get_value(dict, key):
	for values in dict:
		if key in dict:
			value = dict[key]
			try:
				print(value)
				return value
			except KeyError:
				return 0
	return 0


# (dict -> int)
# return the sum of all values found in the dictionary
# the form of the given dictionary is {str: int}
def sum_values(dict):
	sum = 0
	
	for values in dict.values():
		sum += values
	print(sum)
	return sum

# (dict, str -> int)
# return the value for the item with the given key divided by
# the sum of all values found in the dictionary; return 0
# if the sum of all values is 0 (or the dictionary is empty)
# the form of the given dictionary is {str: int}
def frequency_percentage(dict, key):
	summy = sum_values(dict)
	dict_key = get_value(dict, key)

	try:
		return dict_key/summy
	except ZeroDivisionError:
		return 0

	print("fix me")


########################
### PART 2 FUNCTIONS ###

def test_frequency_dictionary():
	print("testing frequency_dictionary")
	dict = frequency_dictionary("thisIsNotaFileName")
	print_test("testing with file that doesn't exist", dict=={})
	dict = frequency_dictionary("hello.txt")
	expected = {"hello": 1}
	print_test("testing with hello.txt", dict==expected)
	dict = frequency_dictionary("birthday.txt")
	expected = {'happy': 4, 'birthday': 4, 'to': 4, 'you': 3, 'CSC110-Class': 1}
	print_test("testing with birthday.txt", dict==expected)
	dict = frequency_dictionary("that.txt")
	expected = {'that': 6, 'exists': 4, 'in': 2}
	print_test("testing with that.txt", dict==expected)
	dict = frequency_dictionary("woodchuck.txt")
	expected = {'how': 1, 'much': 2, 'wood': 4, 'would': 2, 'a': 5,
				'woodchuck': 5, 'chuck': 5, 'if': 2, 'could': 3, 'as': 2}
	print_test("testing with woodchuck.txt", dict==expected)
	print()

# (str -> dict)
# reads from the file given by filename; returns an empty dictionary if
# the file is not found. Otherwise create and return a dictionary with
# the form {str: int} where the strings are words found in the file,
# and the int is how many times the word was found in the dictionary
def frequency_dictionary(filename):
	dict = {}
    
	try:
		file_handle = open(filename, "r")
		print("successfully opened file")
	except FileNotFoundError:
		print('file not found')
		return dict   
	
	for line in file_handle:
		line = line.strip()
		words = line.split(" ")
        
		for word in words:
			if word in dict:
				dict[word] = dict[word] + 1 
			else:
				dict[word] = 1 
	return dict 
        
	
########################
### PART 3 FUNCTIONS ###

def test_dict_to_list():
	dict0 = {}
	result = dict_to_list(dict0)
	print_test("Testing with empty dictionary", result==[])

	dict1 = {'happy': 4, 'birthday': 4, 'to': 4, 'you': 3, 'CSC110-Class': 1}
	result = dict_to_list(dict1)
	expected = [('happy',4),('birthday',4),('to',4),('you',3),('CSC110-Class',1)]
	print_test("Testing with dict1", result==expected)

	dict2 = {'that': 6, 'exists': 4, 'in': 2}
	result = dict_to_list(dict2)
	expected = [('that',6), ('exists',4), ('in',2)]
	print_test("Testing with dict2", result==expected)
	print()

def test_swap():
	print("testing swap")
	dict0 = []
	result = swap(dict0, 3, 4)
	print_test("Testing with empty dictionary", result==[])
    
	dict1 = [10, 7, 8, 9, 6, 5]
	result = swap(dict1, 1, 3)
	expected = [10, 9, 8, 7, 6, 5]
	print_test("Testing with dict1" , result == expected)
    
	dict2 = [ "a", "e", "c", "d", "b" ]
	result = swap(dict2, 1, 4)
	expected = [ "a", "b", "c", "d", "e" ]
	print_test("Testing with dict2", result== expected)
    
	dict3 = [ "Happy" , "to" , "Birthday" , "you" ] 
	result = swap(dict3, 1, 2)
	expected = ["Happy" , "Birthday", "to" , "you"]
	print_test("Testing with dict3", result == expected) 
	

def test_find_max_index_from():
	print("testing find_max_index_from")
    
	dict0 = [] 
	result = find_max_index_from(dict0 , 3)
	expected = -1
	print_test("Testing with empty dictionary", result == expected)
    
	dict1 = [ ('I', 2 ), ('like', 4), ('tuples', 9)] 
	result = find_max_index_from( dict1, 1 )
	expected = ( 2 )
	print_test("Testing with dict1", result == expected)
    
	dict2 = [('out' , 3), (' of', 4), ('range',1)]
	result = find_max_index_from(dict2, 8)
	expected = -1
	print_test("Testing with out of range", result == expected)
	


def test_selection_sort():
	print("testing selection_sort")
    
	dict0 = []
	result = selection_sort(dict0)
	expected = []
	print_test("Testing with empty list", result == expected)
    
	dict1 = [('I',2), ('love', 3), ('CSC110-Class',1)]
	result = selection_sort(dict1)
	expected = [('CSC110-Class',1), ('I',2), ('love',3)]
	print_test ("Testing I love CSC110-Class", result == expected)
    
	dict2 = [('one', 1)] 
	result = selection_sort(dict2)
	expected = [('one',1)]
	print_test("Testing with one", result == expected)
    


# (dict -> (list of tuple))
# creates and returns a new list of tuples with form (str, int)
# taken from the dictionary with elements of the form {str: int}
def dict_to_list(dict):
	list = [(key , value) for key , value in dict.items()] 
	return list 

# (list of tuple), int, int -> None)
# swaps the element in the list at index i1 with the element at index i2
def swap(list, i1, i2):
	if len(list) == 0:
		#print(list)
		return [ ]
	else:
		list[i1], list[i2] = list[i2], list[i1]
		#print(list)
		return list 

# ((list of tuple), int -> int)
# returns the index of the element with the largest integer value in the
# the given list of tuples where tuples have form (str, int)
# returns -1 if an index outside the range of the list is given
def find_max_index_from(list, start_index):
	if len(list) == 0 or start_index < 0 or start_index > len(list):
		return -1
        
	max_index = start_index
	for x in range(start_index, len(list)):
		if list[x][1] > max_index:
			max_index = x
        
	return max_index

# ((list of tuple) -> None)
# sorts the given list using the selection sort algorithm
def selection_sort(list):
	lst = len(list)  
	for x in range(0, lst):  
          
		for i in range(0, lst-x-1):  
			if (list[i][1] > list[i + 1][1]):  
				swap(list, i , i +1) 
	return list 

########################
### PART 4 FUNCTIONS ###

def test_write_most_frequent():
	print("testing write_most_frequent")
	list1 = [("a",27), ("bc",25), ("defg",21), ("hi",21), ("jk",18),
			 ("l",17), ("m",16), ("nop", 15), ("qr", 14), ("s", 13),
			 ("t",10), ("uv",9), ("x",5), ("yz",2)]
	write_most_frequent("test_output.txt", list1, 5, "Alphabet Statistics")
	# Should append to a file called test_output.txt the following:
	# Results for Alphabet Statistics:
	# a: 27
	# bc: 25
	# defg: 21
	# hi: 21
	# jk: 18

	write_most_frequent("test_output.txt", list1, 12, "Large Alphabet Statistics")
	# Should append to a file called test_output.txt the following:
	# Results for Large Alphabet Statistics:
	# a: 27
	# bc: 25
	# defg: 21
	# hi: 21
	# jk: 18
	# l: 17
	# m: 16
	# nop: 15
	# qr: 14
	# s: 13
	# t: 10
	# uv: 9


# (str, (list of tuple), int, str -> None)
# appends to the file named filename data from the first
# n elements found in the given list; assumes the list is sorted;
# the title given should be written on its own line first
def write_most_frequent(filename, list, n, title):
	file_handle = open(filename, "a+")
	file_handle.write(title)
	file_handle.write("\n")
	for x in range (0, n):
		file_handle.write(str(tuple(list[x])))
		file_handle.write("\n")
	file_handle.close()


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
