# assignment7.py
#
# Student name: Naum Hoffman
# Student id:  V00927502

tests = 0
passed = 0

def main():
	test_find_longest()
	test_get_frequency()
	test_is_mutation()
	test_break_mutation()
	test_count_total_mutations()
	test_frequency_incl_mutations()
	file_handle = get_file()
	lom = make_list(file_handle)
	print(lom)

	print("TEST RESULTS:", passed, "/", tests)

def test_find_longest():
	print("testing find_longest")

	lom1 = ["AC", "TACG", "AAC", "GTT"]
	result = find_longest(lom1)
	print_test("find_longest(lom1)", result=="TACG")

	lom2 = ["TG", "TGA", "ACT", "GA", "CCT"]
	result = find_longest(lom2)
	print_test("find_longest(lom2)", result=="TGA")

	lom3 = ["TG", "TTTGAA", "ACT", "CCGA", "CCTAG"]
	result = find_longest(lom3)
	print_test("find_longest(lom3)", result=="TTTGAA")
	print()

def test_get_frequency():
	print("testing get_frequency")

	lom1 = ["AC", "TAC", "GAC", "AC", "GTAC"]
	result = get_frequency(lom1, "AC")
	print_test("get_frequency(lom1, \"AC\")", result==2)

	lom2 = ["ACTG", "TGA", "TTGA", "TGGGGA", "TGAC"]
	result = get_frequency(lom2, "TGA")
	print_test("get_frequency(lom2, \"TGA\")", result==1)

	lom3 = ["GA", "AAG", "AGG", "AGT", "CAG"]
	result = get_frequency(lom3, "AG")
	print_test("get_frequency(lom3, \"AG\")", result==0)

	lom4 = ["AG", "GA", "AAG", "AGG", "AGT", "CAG", "AG", "AG"]
	result = get_frequency(lom4, "AG")
	print_test("get_frequency(lom4, \"AG\")", result==3)
	print()

def test_is_mutation():
	print("testing is_mutation")

	result = is_mutation("ACTG")
	print_test("testing with ACTG", result==False)
	result = is_mutation("ACTGG")
	print_test("testing with ACTGG", result==True)
	result = is_mutation("AACTG")
	print_test("testing with AACTG", result==True)
	result = is_mutation("ACCCCCTG")
	print_test("testing with ACCCCCTG", result==True)
	result = is_mutation("GA")
	print_test("testing with GA", result==False)
	print()

def test_break_mutation():
	print("testing break_mutation")

	result = break_mutation("GTAC")
	print_test("testing with GTAC", result=="GTAC")
	result = break_mutation("GGGTAC")
	print_test("testing with GGGTAC", result=="GTAC")
	result = break_mutation("CGATTT")
	print_test("testing with CGATTT", result=="CGAT")
	result = break_mutation("AAAACC")
	print_test("testing with AAAACC", result=="AC")
	result = break_mutation("TTTTTTTTTTAAGGGGGGG")
	print_test("testing with TTTTTTTTTTAAGGGGGGG", result=="TAG")
	print()

def test_count_total_mutations():
	print ("testing count_total_mutations")

	lom1 = ["AC", "CGT", "TCA", "ATG", "GTAC", "GA"]
	result = count_total_mutations(lom1)
	print_test("testing with lom1", result==0)

	lom2 = ["ACTG", "TGA", "TTGA", "TGGGGGAA", "TGAC"]
	result = count_total_mutations(lom2)
	print_test("testing with lom2", result==2)

	lom3 = ["CCAAAATT", "GGGTT", "AAAATTGGGCCCC", "GGGTT", "GTA"]
	result = count_total_mutations(lom3)
	print_test("testing with lom3", result==4)
	print()

def test_frequency_incl_mutations():
	print ("testing frequency_incl_mutations")

	lom1 = ["AC", "TAC", "ACG", "AC", "GTAC"]
	result = frequency_incl_mutations(lom1, "TA")
	print_test("Testing with lom1 and TA", result==0)
	result = frequency_incl_mutations(lom1, "AC")
	print_test("Testing with lom1 and AC", result==2)

	lom2 = ["TGA", "TTGA", "TGGGGGAA", "TGAA"]
	result = frequency_incl_mutations(lom2, "TGA")
	print_test("testing with lom2 and TGA", result==4)

	lom3 = ["TGAC", "TGA", "TTGA", "TGGGGGAA", "CTGA", "TGAA"]
	result = frequency_incl_mutations(lom3, "TGA")
	print_test("testing with lom3 and TGA", result==4)
	print()

# ((list of str) -> str)
# return the longest string found in the given list
def find_longest(lom):
	for x in range(0, len(lom)):
		return max(lom, key=len)

# ((list of str), str -> int)
# return a count of the total number of times the given
# string is found in the given list of strings
def get_frequency(lom, s):
	count = 0
	for i in range(len(lom)):
		if lom[i] == s:
			count+=1
	print(count)
	return count 


# (str -> bool)
# return True if the given string has any letters
# that occur 2 or more times in a row, False otherwise
def is_mutation(m):
	for i in range(len(m) - 1):
		if m[i] == m[i+1]:
			return True
	return False

# (str -> str)
# return a string with all of the duplicate letters removed
# ASSUME: any duplicate letters will occur in a row
def break_mutation(m):
	notduplicate = ""
	for i in m:
		if not(i in notduplicate):
			notduplicate = notduplicate + i
	
	print(notduplicate)
	return notduplicate
# ((list of str) -> int)
# return a count of the total number of strings with
# duplicate letters in a row in the given list
def count_total_mutations(lom):
	count = 0
	for i in lom:
		if is_mutation(i) == True:
			count +=1 
	return count


# ((list of str), str -> int)
# return a count of the total number of times the given
# string (with duplicates removed) is found in lom
def frequency_incl_mutations(lom, s):
	count = 0
	for i in range(0, len(lom)):
		if lom[i] == s or is_mutation(lom[i]):
			count += 1
	print(count)
	return count


# (None -> File)
# repeatedly prompts the user to enter a file name
# until a file with that name is found to read
def get_file():
	xfiles = False
	while xfiles != True:
		try:
			file_name = input("what file would you like to open? ")
			file_handle = open(file_name, "r")
			xfiles = True
			print("successfuly opened file!")
			return file_handle
		except FileNotFoundError:
			print('file not found')

# (file -> (list of string))
# create and return a new list containing
# all the strings found in the file
def make_list(data_file):
	content = data_file.read()
	list = content.split()
	return list







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
