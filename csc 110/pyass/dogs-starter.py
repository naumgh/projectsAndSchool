import Dog as d
tests = 0
passed = 0
THRESHOLD = 0.1
'''Download dogs.csv. This file contains information
about a number of dogs. Each line of the file contains:
the species of the dog, the name of the dog, and the
vaccinations that dog has had.'''

'''Create a way to store the information from the file
in your program. Remember: each line in the input file
represents information for a single dog'''

def main():
	#test_make_list()
	#test_get_names()
	#test_avg_vaccines()
	test_most_vaccines()
	print("TEST RESULTS:", passed, "/", tests)

def test_make_list():
	print("testing make_list")
	list1 = make_list("no_file.txt")
	print_test("testing with no file", list1==[])

	list2 = make_list("dogs.csv")
	expected = [d.Dog("Lucy", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Polly", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Beast", "chihuaua", ['DHPP-1']), \
				d.Dog("Drake", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Doodle", "poodle", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Dora", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Jessie", "lab", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Rover", "spaniel", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Snuggles", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Yippy", "chihuaua", ['DHPP-1', 'Rabies-1', 'DHPP-2'])]
	print_test("testing with dogs.csv", list2==expected)
	print()

# (str -> (list of Dogs))
# create and return a list of dogs based on the
# data found in the file with the given filename
def make_list(filename):
	lista = []
	try:
		file_handle = open(filename, 'r')
	except FileNotFoundError:
		return []
	for line in file_handle:
		line = line.rstrip('\n')
		line = line.split(',')
		species = line[0]
		name = line[1]
		vaccines = line[2:]
		dog = d.Dog(name, species, vaccines)
		lista.append(dog)
	#print(lista)
	return lista





'''Use the data found in dogs.csv, answer the following:'''

'''Q1: what are the names of all of the dogs?'''

def get_names(lon):
	dog_names = []
	for d in lon:
		name = d.get_name()
		dog_names.append(name)
	print(dog_names)
	return dog_names


def test_get_names():
	print("testing get_names")



	list2 = [d.Dog("Lucy", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Polly", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Beast", "chihuaua", ['DHPP-1']), \
				d.Dog("Drake", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Doodle", "poodle", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Dora", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Jessie", "lab", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Rover", "spaniel", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Snuggles", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Yippy", "chihuaua", ['DHPP-1', 'Rabies-1', 'DHPP-2'])]
	
	result = get_names(list2)	
	expected = ["Lucy", "Polly", "Beast", "Drake", "Doodle","Dora", "Jessie","Rover", "Snuggles", "Yippy"]	
	print_test("testing with dogs.csv", result==expected)
	print()





'''Q2: What is the average number of vaccinations
that these dog have had?'''
def test_avg_vaccines():
	print("testing avg_vaccines")



	list2 = [d.Dog("Lucy", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Polly", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Beast", "chihuaua", ['DHPP-1']), \
				d.Dog("Drake", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Doodle", "poodle", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Dora", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Jessie", "lab", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Rover", "spaniel", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Snuggles", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Yippy", "chihuaua", ['DHPP-1', 'Rabies-1', 'DHPP-2'])]
	
	result = get_avg_vaccines(list2)	
	expected = 3.2
	print_test("testing with avg vaccines", result==expected)
	print()




def get_avg_vaccines(lon):
	total_dogs = 0
	total_vaccines = 0
	for line in lon:
		vac = line.get_vaccines()
		total_dogs += 1
		print(vac)
		for item in vac:
			total_vaccines += 1

	print(total_vaccines)
	print(total_dogs)
	print(total_vaccines/total_dogs)
	return total_vaccines/total_dogs


'''Q3: What is the name and breed of the dog(s)
with the most vaccinations?'''


def test_most_vaccines():
	print("testing most_vaccines")
	list2 = [d.Dog("Lucy", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Polly", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Beast", "chihuaua", ['DHPP-1']), \
				d.Dog("Drake", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Doodle", "poodle", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Dora", "lab", ['DHPP-1', 'Rabies-1']), \
				d.Dog("Jessie", "lab", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2', 'DHPP-3']), \
				d.Dog("Rover", "spaniel", ['DHPP-1', 'Rabies-1', 'DHPP-2']), \
				d.Dog("Snuggles", "pug", ['DHPP-1', 'Rabies-1', 'DHPP-2', 'Rabies-2']), \
				d.Dog("Yippy", "chihuaua", ['DHPP-1', 'Rabies-1', 'DHPP-2'])]
	
	result = most_vaccines(list2)	
	expected = [("Drake","pug"),("Jessie","lab")]
	print_test("testing with most vaccines", result==expected)
	print()


def most_vaccines(lon):
	list1 = []
	current_highest = 0
	highest = 0
	
	if len(lon) == 0:
		return("None","None")
	for line in lon:
		vaccines = line.get_vaccines()
		print(vaccines)
		length = len(vaccines)
		if current_highest < length:
			current_highest = length




	for line in lon:
		vaccines = line.get_vaccines()
		length = len(vaccines)		
		if current_highest == length:
			list1.append((line.get_name(), line.get_species()))
	print(list1)
	return list1






	






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
