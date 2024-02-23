# assignment6.py
#
# Student name:Naum Hoffman
# Student id:  V00927502

tests = 0
passed = 0

def main():
	test_new_double_list()
	test_double_existing_list()
	test_count_multiples()
	test_sum_positive()
	test_add_prefix()
	test_all_long_enough()
	test_growing_strings()

	print("TEST RESULTS: ", passed, "/", tests, sep="")

def test_new_double_list():
	print("testing new_double_list")
	list1 = []
	result = new_double_list(list1)
	print_test("testing list1 unchanged", list1==[])
	print_test("testing value returned with empty", result==[])

	list2 = [3, 8, 4, 7]
	result = new_double_list(list2)
	print_test("testing list2 unchanged", list2==[3,8,4,7])
	print_test("testing value returned with list2", result==[6,16,8,14])

	list3 = [5, 9, 2, 3]
	result = new_double_list(list3)
	print_test("testing list3 unchanged", list3==[5,9,2,3])
	print_test("testing value returned with list3", result==[10,18,4,6])
	print()

	list4 = [10, 9, 5, 6, 2, 3, 7]
	result = new_double_list(list3)
	print_test("testing list3 unchanged", list3==[5,9,2,3])
	print_test("testing value returned with list3", result==[10,18,4,6])
	print()

def test_double_existing_list():
	print("testing double_existing_list")
	list1 = []
	double_existing_list(list1)
	print_test("testing with empty list", list1==[])
	list2 = [3, 8, 4, 7]
	double_existing_list(list2)
	print_test("testing with list2", list2==[6,16,8,14])
	list3 = [5, 9, 2, 3]
	double_existing_list(list3)
	print_test("testing with list3", list3==[10,18,4,6])
	print()

def test_count_multiples():
	print("testing count_multiples")
	list1 = []
	result = count_multiples(list1, 2)
	print_test("testing with empty and 2", result==0)
	print("testing count_multiples")
	list1 = [7, 2, 9]
	result = count_multiples(list1, 9)
	print_test("testing with list and 9", result==1)
	# add more tests
	print()

def test_sum_positive():
	print("testing sum_positive")
	list1 = []
	result = sum_positive(list1)
	print_test("testing with empty", result==0)
	print("testing sum_positive")
	list2 = [2, 3, 4, 5]
	result = sum_positive(list2)
	print_test("testing with empty", result==14)
	# add more tests
	print()

def test_add_prefix():
	print("testing add_prefix")
	list1 = []
	add_prefix(list1, "un")
	print_test("testing with empty list and un", list1==[])

	list2 = ["zip", "real", "likely", "veil"]
	add_prefix(list2, "un")
	expected = ["unzip", "unreal", "unlikely", "unveil"]
	print_test("testing with list2 and un", list2==expected)

	list3 = ["fine", "lay", "spite", "tail"]
	add_prefix(list3, "re")
	expected = ["refine", "relay", "respite", "retail"]
	print_test("testing with list3 and re", list3==expected)

	list3 = ["fine", "lay", "spite", "tail"]
	add_prefix(list3, "de")
	expected = ["define", "delay", "despite", "detail"]
	print_test("testing with list3 and de", list3==expected)
	print()


def test_all_long_enough():
	print("testing all_long_enough")
	list1 = []
	result = all_long_enough(list1, 0)
	print_test("testing with empty and 0", result==True)

	list2 = ["this", "is", "so", "fun"]
	result = all_long_enough(list2, 3)
	print_test("testing with 0", result==False)
	# add more tests
	print()

def test_growing_strings():
	print("testing growing_strings")
	list1 = []
	result = growing_strings(list1)
	print_test("testing with empty list", result==True)
	
	print("testing growing_strings")
	list2 = ["gang"]
	result = growing_strings(list2)
	print_test("testing with empty list", result==True)

	print("testing growing_strings")
	list3 = ["n", "na", "nau", "naum"]
	result = growing_strings(list3)
	print_test("testing with empty list", result==True)
	
	print("testing growing_strings")
	list4 = ["n", "nau", "na", "naum"]
	result = growing_strings(list4)
	print_test("testing with empty list", result==False)
	print()

#creates a new list and doubles it
#(list)->list
def new_double_list(lon):
	newaList = []
	lista = []
	for t in range(0, 1):
		for x in range(0, len(lon)):
			newaList = lon[x] * 2
			lista.append(newaList)
		print(lista)
		return(lista)


#doubles an existing list
#(list)->list
def double_existing_list(lon):
	for t in range(0, len(lon), 1):
		lon[t] *= 2

	print(lon)


#counts the amount of times n is in a list
#(list, int)->list
def count_multiples(lon, n):
	count = 0
	for t in range(0, len(lon), 1):
		if lon[t] == n:
			count += 1
			print(count)
	return count

#adds all the positive ints in a list
#(list)->int
def sum_positive(lon):
	count = 0
	for t in range(0, len(lon), 1):
		if lon[t] > 0:
			count = lon[t] + count
	return count		


#adds a prefix in front of all words in a staring and returns it
#(list, String)->list
def add_prefix(los, prefix):
	for t in range(0, len(los), 1):
		String1 = prefix + los[t]
		los[t] = String1
	print(los)
	return los
		

#tests to see if all strings in a list are long enough
#(list,int)->list
def all_long_enough(lon, n):
	for t in range(0, len(lon), 1):
		print(lon[t])
		if len(lon[t]) < n:
			return False
	return True

		

#tests to see if every part of string in numerical order
#(list)->list
def growing_strings(los):
	u = len(los)
	for t in range(0, u-1, 1):	
		if los[t] > los[t + 1]:
			return False
	return True
	

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
