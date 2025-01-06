tests = 0
passed = 0

def main():
	test_make_list()
	#test_create_with_only()
	#test_negate_first()
	#test_add1_to_all()
	#test_make_all_positive()
	test_is_decreasing()
	test_min_value()
	print("Test results:", passed, "/", tests)

''' Q1: Design a function that creates a list and repeatedly
asks the user for positive integers and adds these numbers
to a list. The user enters no more numbers by entering a 0.
The function should return the list in the end. Assume the
user enters only numerical values'''

def test_make_list():
	result = make_list()
	print(result)
	print()

# Complete the function design
def make_list():
	...

''' Q2: Design a function that will take a list of words and a
letter as a String and return a new list with only words that
start with that letter. Assume words in the list are not empty
strings and the letter is of length 1.'''

def test_create_with_only():
	print("testing create_with_only")
	list1 = ["abc", "cde", "jkl", "asdf", "azq"]
	result = create_with_only(list1, "x")
	print_test("testing list1 with x", result==[])
	result = create_with_only(list1, "c")
	print_test("testing list1 with c", result==["cde"])
	result = create_with_only(list1, "a")
	print_test("testing list1 with a", result==["abc", "asdf", "azq"])
	list2 = ["csc110", "is", "the", "best", "class"]
	result = create_with_only(list2, "c")
	print_test("testing list2 with c", result==["csc110", "class"])
	print()

# Complete the function design
def create_with_only(los, letter):
	...

''' Q3: Design a function that will change the first element
in the given list of integers to it's negated value. For example:
if the value is 8, change it -8, if the value is -2 change it to 2'''

def test_negate_first():
	print ("testing negate_values")
	empty_list = []
	negate_first(empty_list)
	print_test("negate_first(empty_list)", empty_list == [])

	list_1 = [3]
	negate_first(list_1)
	print_test("negate_first(list_1)", list_1 == [-3])

	list_3 = [-7, 9, 11]
	negate_first(list_3)
	print_test("negate_first(list_3)", list_3 == [7,9,11])
	print()



# Complete the function design
def negate_first(nums):
	
	if len(nums[0] > 0):
		nums[0] *= -1
	#return nums

''' Q4: Design a function a function that adds one to
every element in the given list'''

def test_add1_to_all():
	print("Testing add1_to_all")
	empty_list = []
	list1 = [3, 7, 1]
	list2 = [9, -4, 8, 6, -3]
	add1_to_all(empty_list)
	print_test("testing with empty", empty_list==[])
	add1_to_all(list1)
	print_test("testing with [3, 7, 1]", list1==[4,8,2])
	add1_to_all(list2)
	print_test("testing with [9,-4,8,-6,3]", list2==[10,-3,9,7,-2])
	print()

# ((list of int) -> None)
# modify given list by adding 1 to each element
def add1_to_all(lon):
	...

''' Q5: Design a function that will take a list of integers
and change every value in that list to it's absolute value.
DO NOT use the built in absolute value function.'''

def test_make_all_positive():
	print("Testing make_all_positive")
	empty_list = []
	list1 = [-3, -7, 1]
	list2 = [9, -4, 8, 6, -3]
	make_all_positive(empty_list)
	print_test("testing with empty", empty_list==[])
	make_all_positive(list1)
	print_test("testing with [-3, -7, 1]", list1==[3,7,1])
	make_all_positive(list2)
	print_test("testing with [9,-4,8,-6,3]", list2==[9,4,8,6,3])
	print()

# ((list of int) -> None)
# modify given list by changing all negative values to positive
def make_all_positive(lon):
	...



'''Q7: Design a function that will take a list of
integers and determines whether the numbers in that
list are strictly decreasing by 1. '''

def test_is_decreasing():
	print("Testing is_decreasing")
	empty_list = []
	list1 = [5,4,3,2]
	list2 = [5,4,3,0]
	list3 = [5,6,7,8]
	list4 = [8,7,4,3]
	list5 = [2,1,0,-1,-2]
	result = is_decreasing(empty_list)
	print_test("testing with empty list", result==True)
	result = is_decreasing(list1)
	print_test("testing with [5,4,3,2]", result==True)
	result = is_decreasing(list2)
	print_test("testing with [5,4,3,0]", result==False)
	result = is_decreasing(list3)
	print_test("testing with [5,6,7,8]", result==False)
	result = is_decreasing(list4)
	print_test("testing with [8,7,4,3]", result==False)
	result = is_decreasing(list5)
	print_test("testing with [2,1,0,-1,-2]", result==True)
	print()

# ((list of int) -> bool)
# return True if all elements in lon decrease in order by 1
def is_decreasing(lon):
	if len(lon) == 0:
		return True
	prev = lon[0]
	for n in lon[1:]:
		if(prev != n + 1):
			return False
		prev = n
	return True 



	#for x in range(0, len(lon)):
		#if lon[x] == lon[x+1] +1:
		#	print(lon[x])
		#	return True
		#else:
		#	return False

def test_min_value():
	print("testing test_min_value")
	list1 = [8, 6, 9, 4, 2, 5, 3]
	list2 = [4, 7, 9, 5, 7, 1]

	result = min_value(list1)
	print_test("testing with a list", result== 2)
	result = min_value(list2)
	print_test("testing with a list", result== 1)

def min_value(lon):
	min = 0
	for n in range(0, len(lon), 1):
		if lon[n] > n +1:
			min = lon[n+1]
			print(min)
	print(min)
	return min

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
