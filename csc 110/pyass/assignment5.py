# assignment5.py
#
# Student name: Naum Hoffman
# Student id:  V00927502

tests = 0
passed = 0

def main():
	test_is_prime()
	test_count_primes()
	test_sum_digits()

	print("TEST RESULTS: ", passed, "/", tests, sep="")

def test_is_prime():
	print("testing is_prime")
	result = is_prime(3)
	print_test("Testing with 3", result==True)
	result = is_prime(2)
	print_test("Testing with 2", result==True)
	result = is_prime(4)
	print_test("Testing with 4", result==False)
	result = is_prime(8)
	print_test("Testing with 8", result==False)
	result = is_prime(-4)
	print_test("Testing with -4", result==False)
	result = is_prime(-9)
	print_test("Testing with -9", result==False)


def test_count_primes():
	print ("testing count primes")
	result = count_primes(3, 11) # primes: 3, 5, 7, 11
	print_test("testing with 3, 11", result==4)
	result = count_primes(1, 20) # primes: 2, 3, 5, 7, 11, 13, 17, 19
	print_test("testing with 1, 20", result==8)
	result = count_primes(3, 4) # primes: 3, 5
	print_test("testing with 3, 4", result==1)
	result = count_primes(3, 11) # primes: 3, 5, 7, 11
	print_test("testing with 3, 11", result==4)
	result = count_primes(-2, 11) # primes: -2, 3, 5, 7, 11
	print_test("testing with -2, 11", result==6)
	

def test_sum_digits():
	print("testing sum_digits")
	result = sum_digits(4)
	print_test("testing with 4", result==4)
	result = sum_digits(469)
	print_test("testing with 469", result==19)
	result = sum_digits(777)
	print_test("testing with 469", result==21)
	result = sum_digits(468)
	print_test("testing with 469", result==18)
	

# (int -> bool)
# returns True if n is prime, False otherwise
def is_prime(n):
	count = 0
	for i in range(0, abs(n)):
		for i in range(1, abs(n) + 1, 1):
			#print(n%i)
			if(n == 0 or n == 1):
				return False

			if abs(n % i) == 0:
				count += 1
				#count += count
		if count == 2:
			#print(count)
			return True
		else:
			#print(count)
			return False






# (int, int -> int)
# returns the number of prime numbers found within the
# range of the two given numbers (inclusive)
def count_primes(num1, num2):
	count = 0
	for i in range(num1, num2):
		
		if is_prime(i) == True:
			count += 1
	if is_prime(num2) == True:
		count+=1
			

	print(count)
	return count



	



# (int -> int)
# returns the sum of all the digits in the given number
# ASSUME: the value is a positive, whole number.
def sum_digits(n):
	# TODO: implement this function (and erase this comment)
	sum = 0
	while n != 0:
		sum += n % 10 
		n //= 10 
	return sum


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
