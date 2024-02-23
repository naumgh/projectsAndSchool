tests = 0
passed = 0

def main():
	test_sum_list()
	#test_count_odd()
	#test_contains_value()
	#test_count_duplicates()
	print("Test results:", passed, "/", tests)

''' 
Design a function that takes a list of integers and
returns a sum of all of elements found in the list
'''

def test_sum_list():
	print ("testing sum_list")
	list1 = []
	list2 = [2, 18, 7, 3, 5]
	list3 = [9, 5, 4, 7, 2, 1, 14, 6]
	result = sum_list(list1)
	print_test("testing with empty", result==0)
	result = sum_list(list2)
	expected = 2+18+7+3+5
	print_test("testing with [2, 18, 7, 3, 5]", result==expected)
	result = sum_list(list3)
	expected = 9+5+4+7+2+1+14+6
	print_test("testing with [9, 5, 4, 7, 2, 1, 14, 6]", result==expected)
	print()

# ((list of int) -> int)
# returns the sum of all values in the given list of numbers
def sum_list(lon):
	for i in range(1, len(lon)):
		sumo += lon[i]


	return sumo


''' Design a function that takes a list of numbers and returns
the number of odd values found in the list'''

def test_count_odd():
	print("testing count_odd")
	list1 = []
	list2 = [2, 18, 7, 3, 5]
	list3 = [9, 5, 4, 7, 2, 1, 14, 6]
	result = count_odd(list1)
	print_test("testing with empty", result==0)
	result = count_odd(list2)
	print_test("testing with [2, 18, 7, 3, 5]", result==3)
	result = count_odd(list3)
	print_test("testing with [9, 5, 4, 7, 2, 1, 14, 6]", result==4)
	print()

# complete the function design:
def count_odd(lon):
	...


''' Design a function that takes two parameters: a list of
numbers and a single value. The function should determine
if the value is found in the list. '''

def test_contains_value():
	print("testing contains value")
	list1 = []
	list2 = [2, 18, 7, 3, 5]
	list3 = [9, 5, 4, 7, 2, 1, 14, 6]
	result = contains_value(list1, 3)
	print_test("testing if empty contains 3", result==False)
	result = contains_value(list2, 3)
	print_test("testing if [2, 18, 7, 3, 5] contains 3", result==True)
	result = contains_value(list2, 4)
	print_test("testing if [2, 18, 7, 3, 5] contains 3", result==False)
	result = contains_value(list3, 6)
	print_test("testing if [9, 5, 4, 7, 2, 1, 14, 6] contains 6", result==True)
	result = contains_value(list3, 0)
	print_test("testing if [9, 5, 4, 7, 2, 1, 14, 6] contains 0", result==False)
	print()

# complete function design
def contains_value(lon, v):
	#count = 0
	#if()

''' 
Design a function that takes two lists as parameters
and returns a count of how many of the elements in the first
list are found in the second list 

'''

def test_count_duplicates():
	print("testing count duplicates")
	list1 = []
	list2 = [2, 18, 7, 3, 5]
	list3 = [9, 5, 4, 7, 2, 1, 14, 6]
	list4 = [1, 2, 3, 4]
	result = count_duplicates(list1, list1)
	print_test("testing with empty and empty", result==0)
	result = count_duplicates(list1, list2)
	print_test("testing with empty and [2, 18, 7, 3, 5]", result==0)
	result = count_duplicates(list2, list1)
	print_test("testing with [2, 18, 7, 3, 5] and empty", result==0)
	result = count_duplicates(list4, list2)
	print_test("testing with [1, 2, 3, 4]\n\tand [2, 18, 7, 3, 5]", result==2)
	result = count_duplicates(list4, list3)
	print_test("testing with [1, 2, 3, 4]\n\tand [9, 5, 4, 7, 2, 1, 14, 6]", result==3)
	result = count_duplicates(list2, list3)
	print_test("testing with [2, 18, 7, 3, 5]\n\tand [9, 5, 4, 7, 2, 1, 14, 6]", result==3)
	print()

# complete the function design
def count_duplicates(lon1, lon2):
	count = 0
	for num in list1:
		if(contains_value(list2, num)):
			count += 1
	return count


	#step 1: make an accumulator
	#step 2: loop through each item in list 1
	#step 3: check if that item is found in list 2
	#if so, add 1 to my accumulator
	#step 4, retrun accumulator after finishing loop


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
