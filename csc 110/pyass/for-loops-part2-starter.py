tests = 0
passed = 0

def main():
	test_get_sum()
	test_reverse_string()
	# result = mystery("Welcome to CSC 110 everyone!")
	# print (result)
	test_count_squares()
	# result = counter(3, 5, 2)
	# print(result)
	print("Test results:", passed, "/", tests)

''' Design a function that takes two who numbers as parameters
and sums all values from the smaller of the two given numbers
up to (and including) the larger one. '''

def test_get_sum():
	print ("testing get_sum")
	result = get_sum(3,8)
	expected = 3+4+5+6+7+8
	print_test("testing with 3, 8", result==expected)
	result = get_sum(8,3)
	expected = 3+4+5+6+7+8
	print_test("testing with 8, 3", result==expected)
	result = get_sum(10, -2)
	expected = (-2)+(-1)+0+1+2+3+4+5+6+7+8+9+10
	print_test("testing with -2, 10", result==expected)

# (int, int -> int)
# returns the sum of all values between num1 and num2
def get_sum(num1, num2):
	sum = 0
	

	min = num1
	max = num2


	if(num1 > num2):
		min = num2
		max = num1

	for i in range(min, max+1):
		sum += i 


	return sum


''' Design a function that takes a string as a parameter
and returns the reverse of that string '''

def test_reverse_string():
	print("testing reverse_string")
	result = reverse_string("computer")
	print_test("testing with computer", result=="retupmoc")
	result = reverse_string("science")
	print_test("testing with science", result=="ecneics")
	result = reverse_string("racecar")
	print_test("testing with racecar", result=="racecar")

# (str -> str)
# returns the given string reversed
def reverse_string(s):
	result = ""
	for i in range(len(s)):
		letter = s[i]
		result = letter + result
		
	print(result)
	return result

'''
What is the output of the code below?

# (str -> int)
# what does this function do?
def mystery(text):
	count = 0
	size = len(text)
	for i in range(size):
		c = text[i]
		if (c.isupper()):
			count += 1
	return count
'''


''' Design a function that takes an integer as a parameter
and returns the number of perfect squares there are up to
and including that number. A perfect square is a number
multiplied by itself: 2x2=4, 3x3=9, 4x4=16, so 4, 9, and 16
are examples of perfect squares). Try using a WHILE loop.'''

def test_count_squares():
	print("testing get_squares")
	result = count_squares(9) # 1, 4, 9
	print_test("testing with 9", result==3)
	result = count_squares(10) # 1, 4, 9
	print_test("testing with 10", result==3)
	result = count_squares(99) # 1, 4, 9, ..., 64, 81
	print_test("testing with 99", result==9)
	result = count_squares(100) # 1, 4, 9, ..., 64, 81, 100
	print_test("testing with 100", result==10)

# (int -> int)
# return a count of the number of perfect squares
# there are up to the given number
def count_squares(n):
	return 0



'''
What is the output of the code below?

# (int, int, int -> int)
# what does this function do?
def counter(num1, num2, n):
	count = 0
	for i in range(1, num1+1):
		for j in range(num1, num2+1):
			num3 = i*j
			if (num3%n == 0):
				count += 1
	return count
'''



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
