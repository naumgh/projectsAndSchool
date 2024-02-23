# (None -> None)
# tries to convert a string into an integer
def convert_to_number():
	course = "csc110"
	print("course is:", course)
	num = int(course)
	print("num is:", num)

# (None -> None)
# accesses an invalid index in a list
def list_bounds():
	lon = [9, 1, 7, 4]
	index = 0
	print("lon[0] is:", lon[index])
	index = 4
	print("lon[4] is:", lon[index])


# (None -> int)
# Asks a user to enter a number and returns the
# number entered if valid, 0 otherwise
def get_number_v1():
	try:
		n = int(input("Enter an integer: "))
		return n
	except ValueError:
		print("there was a value ValueError")
		return 0

	


# (None -> int)
# Repeatedly ask a user to enter a number until
# a valid number is entered; returns the value
def get_number_v2():
	valid_engry = False
	while (valid_engry != True):
		try:
			n = int(input("Enter an integer: "))
			valid_engry = True	
		except ValueError:
			print("invalid entry")
	return n
    

# (None -> File)
# Repeatedly a user to enter a file name until
# a valid file is found and returned
def get_file():
	valid_entry = False

	while valid_entry != True:
		try:
			path = input("Enter file name: ")
			file_handle = open(path, "r")
			return file_handle
		except FileNotFoundError:
			print("could not find that file")


def main():
	convert_to_number()
	list_bounds()
	n = get_number_v1()
	print("Number entered:", n)
	n = get_number_v2()
	print("Number entered:", n)
	file = get_file()
	print(file.readline())

main()
