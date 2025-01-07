# Naum Hoffman
# V00927502


tests = 0
passed = 0

def main():
	test_get_factorial()
	test_get_occurrences()
	test_count_multiples()
	test_print_ten_multiples()
	print("Test results:", passed, "/", tests)



def test_get_factorial():
	print("testing get_factorial...")
	result = get_factorial(0)
	print_test("testing factorial", result==1)
	result = get_factorial(3)
	print_test("testing factorial", result==6)
	result = get_factorial(6)
	print_test("testing factorial", result==720)
	#TODO: add more tests here




def test_get_occurrences():
	print("testing get_occurrences...")
	result = get_occurrences("x","anthony")
	print_test("testing with x and anthony", result==0)
	result = get_occurrences("a","naum")
	print_test("testing with a and naum", result==1)
	result = get_occurrences("b","baby")
	print_test("testing with b and baby", result==2)
	result = get_occurrences("a","aardvark")
	print_test("testing with a and aardvark", result==3)
	#TODO: add more tests here


def test_count_multiples():
	print("testing count_multiples...")
	result = count_multiples(1, 9, 2)
	print_test("testing with 1, 9, 2", result==4)
	result = count_multiples(20, 28, 3)
	print_test("testing with 20, 28, 3", result==3)
	result = count_multiples(10, 20, 2)
	print_test("testing with 10, 20, 2", result==5)
	#TODO: add more tests here


def test_print_ten_multiples():
	print("testing print_ten_multiples")
	print("\nTesting with 3")
	print_ten_multiples(3) #expects row to be 3-30
	print("\nTesting with 11")
	print_ten_multiples(11) #expects row to be 11-110
	print("\nTesting with 7")
	print_ten_multiples(7) #expects row to be 7-70

	#TODO: add more tests here


# TODO: Complete function design
#takes the factorial of a number
#(int) -> int
def get_factorial(n):
	nfactorial = 1
	for i in range(1, n+1):
		if(n == 0):
			return 1
		else:
			nfactorial = nfactorial*i
	
	return nfactorial



# TODO: Complete function design
#(String, String) -> int
#Counts the amount of a certain letter there is in a string
def get_occurrences(c, text):
	count = 0
	for i in range(0, len(text)):
		if(text[i] == c):
			count += 1
	
	return count

		



# TODO: Complete function design
#(int, int, int) -> int
#counts the amount of multiples of a certain number in a range
def count_multiples(start, end, n):
	count = 0
	for i in range(start, end):
		if(i%n == 0):
			count += 1
	return count




# TODO: Complete function design
#(int) -> none
#prints multiples from max to max times 10 and puts it in an array
def print_ten_multiples(max):
	count = 1
	min = 1
	while(count <= max):
		for i in range(min, (count * (11)), count):
			print(format(i, " 3d"), end='')
		count += 1
		min += 1
		print(" ")
	print("")




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
