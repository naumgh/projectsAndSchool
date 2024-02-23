tests = 0
passed = 0

def main():
	#test_sum_tuples_list()
	#test_count_born_in_month()
	#test_born_before()
	test_get_family()

	print("Test results:", passed, "/", tests)

''' Q1: Design a function that returns the sum of all
of the values found in each of the tuples in a given
list of tuples'''

def test_sum_tuples_list():
	print("testing sum_tuples_list")
	list1 = []
	list2 = [(6, 2), (9, 1)]
	list3 = [(1, 2, 3), (6, 4), (8, 5, 1)]

	result = sum_tuples_list(list1)
	print_test("testing with empty", result==0)

	result = sum_tuples_list(list2)
	print_test("testing with list2", result==18)

	result = sum_tuples_list(list3)
	expected = 1+2+3+6+4+8+5+1
	print_test("testing with list3", result==expected)

def sum_tuples_list(lot):
	count = 0
	for x in lot:
		for n in x:
			count += n
	print(count)
	return count
''' Q2: Design a function that takes a list of tuples and a number,
where all tuples represent birth dates. The function returns a
count of the number of birth dates in the list where the birth month
of the tuple is equal to the given number.'''

def test_count_born_in_month():
	print ("testing count_born_in_month")

	# tuples represent birth date: (year, month, day)
	list1 = [(1992, 8, 27), (2001, 2, 4)]
	result = count_born_in_month(list1, 5)
	print_test("testing with list1 and 5", result==0)
	result = count_born_in_month(list1, 8)
	print_test("testing with list1 and 8", result==1)

	list2 = [(2004,  1, 19), (1998, 6, 14), (1994, 7,  1),
			 (2000,  6, 29), (1992, 1,  4), (1999, 6,  2),
			 (2005, 12, 18), (2001, 5, 11), (2000, 7, 22)]
	result = count_born_in_month(list2, 7)
	print_test("testing with list2 and 7", result==2)
	result = count_born_in_month(list2, 6)
	print_test("testing with list2 and 6", result==3)

def count_born_in_month(lot, m):
	count = 0
	for x in lot:
		for n in x:
			if(n == m):
				count += 1
	return count
	print(count)
	print("the number does represent the month", count, "times.")

''' Q3: Design a function that takes a list of tuples and a tuple,
where all tuples represent birth dates. The function returns a
count of the number of birth dates in the list that come before
the given birth date.'''

def test_born_before():
	print ("testing count_born_before")
	# tuples represent birth date: (year, month, day)
	list1 = [(1992, 8, 27), (2001, 2, 4)]

	result = count_born_before(list1, (1996, 9, 29))
	print_test("testing with list1 and (1996, 09, 29)", result==1)

	list2 = [(2004,  1, 19), (1998, 6, 14), (1994, 7,  1),
			 (2000,  6, 29), (1992, 1,  4), (1999, 6,  2),
			 (2005, 12, 18), (2001, 5, 11), (2000, 7, 22)]
	result = count_born_before(list2, (1996, 9, 29))
	print_test("testing with list2 and (1996, 09, 29)", result==2)
	result = count_born_before(list2, (2000, 9, 1))
	print_test("testing with list2 and (2000, 09, 01)", result==6)
	result = count_born_before(list2, (2000, 6, 30))
	print_test("testing with list2 and (2000, 06, 30)", result==5)
	result = count_born_before(list2, (2000, 6, 29))
	print_test("testing with list2 and (2000, 06, 29)", result==4)
	result = count_born_before(list2, (2000, 6, 28))
	print_test("testing with list2 and (2000, 06, 28)", result==4)

'''
def comes_before(date1, date2):
	if date1[0] > date2[0]:
		return True
		elif date1[1] > date2[1]:
			return True
			elif date1[2] > date2[2]:
				return True
				else:
					return False
		
'''


def count_born_before(lot, date):
	count = 0
	for x in lot:
		if(comes_before(touple, date)):
			count += 1
	return count


''' Q4: Design a function that takes a list of tuples and a string,
and returns all tuples that contain the given string'''

def test_get_family():
	print("testing get_family")
	# tuple represent names of family members:
	list1 = [("Alex", "Sam", "Taylor", "Don"),
			 ("Crystal", "Ali", "Maya", "Sam", "Leo"),
			 ("Sean", "Mia"),
			 ("Mei", "Sarah", "Sean", "Ali")]

	result = get_family(list1, "Mia")
	print_test("testing with list1 and Mia", result==[("Sean", "Mia")])
	result = get_family(list1, "Sean")
	expected = [("Sean", "Mia"),
				("Mei", "Sarah", "Sean", "Ali")]
	print_test("testing with list1 and Sean", result==expected)
	result = get_family(list1, "Sam")
	expected = [("Alex", "Sam", "Taylor", "Don"),
				("Crystal", "Ali", "Maya", "Sam", "Leo")]
	print_test("testing with list1 and Sam", result==expected)

# (list of tuple), str -> (list of tuple)
# return a list of all tuples that contain s
def get_family(lot, s):
	listxpected = []
	x = 0
	while x < len(lot):
		for x in range(0, len(lot)):
			if s in lot[x]:
				z = lot[x]
	return z

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
