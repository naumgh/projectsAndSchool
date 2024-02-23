# assignment3.py
#
# Student name: Naum Hoffman	
# Student id:  V00927502

tests = 0
passed = 0

FULL_BATTERY_LIFE = 15

def main():
	print('Assignment 3')
	test_middle_value()
	test_combine_strings()
	test_get_letter_at()
	test_brightness_modifer()
	test_hours_remaining()
	print("TEST RESULTS:", passed, "/", tests)

def test_middle_value():
	print("beginning tests for middle_value...")
	result = middle_value(5, 1, 3)
	print("the middle value is 3")
	print_test("testing middle_value:" , result == 3)
	result = middle_value(1, 5, 3)
	print("the middle value is 3")
	print_test("testing middle_value", result == 3)
	print("the middle value is 4")
	result = middle_value(5, 4, 6)
	print_test("testing middle_value", result == 5)
	
	#TODO: add tests here (and erase this line if you want)
	#tests which number is bigger and returns the result
	#calls test_middle, which returns whether it passes
def middle_value(a, b, c):
	
		if(a >= b >= c or c >= b >= a):
			return b
		elif(c >= a >= b or b >= a >= c):
			return a
		else:
			return c

	#calls combinr_strings and tests whether the result is true of fales
def test_combine_strings():
	print("beginning tests for combine_strings...")
	result = combine_strings("after","thought")
	print("afterthought")
	print_test("testing combine_strings", result == "afterthought")
	result = combine_strings("shell","sea")
	print("seashell")
	print_test("testing combine_strings", result == "seashell")


	#(string, string -> string)
	#compares two strings and tests for the largest one.
	#It then concatinates the two based on the smaller string coming first
def combine_strings(a, b):
	if(len(a) >= len(b)):
		
		return(b+a)
	else:
	
		return(a+b)



def test_get_letter_at():
	print("beginning tests for get_letter_at...")
	print("the letter in the 0 index is N")
	result = get_letter_at("Naum", 0)
	print_test("testing get_letter_at", result == "N")
	result = get_letter_at("Thomas", 2)
	print("the letter in the 2nd index is o")
	print_test("testing get_letter_at", result == "o")
	#TODO: add tests here (and erase this line if you want)

def get_letter_at(string1, int1):
	sentence = string1[int1] 
	return(sentence)

def test_brightness_modifer():
	percent = '%'
	print("beginning tests for brightness_modifer...")
	result = brightness_modifer(0)
	print("there's 100",percent, "battery left, with level 0 brightness")
	print_test('testing brightness_modifer', result == 1.0)
	result = brightness_modifer(1)
	print("there's 90",percent, "battery left, with level 1 brightness")
	print_test('testing brightness_modifer', result == 0.9)
	result = brightness_modifer(2)
	print("there's 75",percent, "battery left, with level 2 brightness")
	print_test('testing brightness_modifer', result == .75)
	result = brightness_modifer(3)
	print("there's 50",percent, "battery left, with level 3 brightness")
	print_test('testing brightness_modifer', result == .5)
	
	#TODO: add tests here (and erase this line if you want)

	#(int -> float )
	#returns the amount of battery left based upon the 
	#brightness of the screen
def brightness_modifer(z):
	
	if(z == 0):
		
		return 1.0
	elif(z == 1):
		
		return 0.9
	elif(z == 2):
		
		return .75
	else:
		
		return .50


	#calls print_test to see whether the result passes or fails
	#calls hours_remaining with 3 types of parameters
def test_hours_remaining():
	print("beginning tests for hours_remaining...")
	result = hours_remaining(80, 2, True)
	print("there are 4.5 hours remaining")
	print_test('testing hours_remaining', result == 4.5)
	result = hours_remaining(25, 2, True)
	print("there are 1.40625 hours remaining")
	print_test('testing hours_remaining', result == 1.40625)
	result = hours_remaining(70, 3, False)
	print("there are 5.25 hours remaining")
	print_test('testing hours_remaining', result == 5.25)
	#TODO: add tests here (and erase this line if you want)
	

	#(int, int, bool -> float)
	#returns the actual amount of time left on the phone
	#based upon whenther the phone is streaming

def hours_remaining(batterypercent, brightness, streaming):
	global FULL_BATTERY_LIFE
	regular_battery = batterypercent/100 * FULL_BATTERY_LIFE
	brightness_level = brightness_modifer(brightness)
	not_streaming = brightness_level * regular_battery
	if(streaming == True):
		return(not_streaming * 0.5)
	else:
		return(not_streaming)
	
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
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
