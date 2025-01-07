import Student as s
tests = 0
passed = 0

def main():
	test_add_grade()
	test_get_average()
	test_average_of_student()
	test_honor_roll()
	print("TEST RESULTS:", passed, "/", tests)

''' Complete the add_grade method in the Student class so that
it adds a grade to the list of grades in a Student object'''
def test_add_grade():
	print("testing add_grade")

	s1 = s.Student("v00123456", [80, 60, 77, 92])
	print(s1)
	old_grades = s1.get_grades()
	print_test("testing original grades length", old_grades==[80, 60, 77, 92])
	s1.add_grade(75)
	new_grades = s1.get_grades()
	print_test("after adding grade grades length updated", new_grades==[80, 60, 77, 92,75])
	print()

''' Complete the get_average method in the Student class so that
it returns the overall average across all grades of a Student object'''
def test_get_average():
	print("testing get_average")

	s1 = s.Student("v00123456", [50,60,70,80])
	avg = s1.get_average()
	print_test("Testing s1's average", avg==(50+60+70+80)/4)

	s2 = s.Student("v00999888", [82, 87, 91, 95, 78])
	avg = s2.get_average()
	print_test("Testing s2's average", avg==(82+87+91+95+78)/5)
	print()

''' Design a function that takes a list of Student objects
and a string representing a student ID as a parameter, and
returns the average grade for that student if a student
with that ID exists in the list. If there is no student with
the given ID, return 0.'''
def test_average_of_student():
	print("testing average_of_student")

	s1 = s.Student("v00987654", [81, 84, 92])
	s2 = s.Student("v00454333", [65, 70, 81])
	s3 = s.Student("v00123456", [75, 80, 85])
	s4 = s.Student("v00678765", [90, 60, 60])
	list1 = [s1, s2, s3, s4]

	result = average_of_student(list1, "v00555678")
	print_test("testing with student not in list", result==0.0)

	result = average_of_student(list1, "v00987654")
	print_test("testing with s1's ID", result==(81+84+92)/3)

	result = average_of_student(list1, "v00678765")
	print_test("testing with s4's ID", result==(90+60+60)/3)
	print()

# ((list of Student), str -> float)
# return the average grade of student with given student ID
def average_of_student(los, id):
	for s in los:
		if s.get_sid() == id:
			return s.get_average()
	return 0.0


''' Design a function that takes a list of Student objects
and returns a list of the students who are on the 'honor roll'.
For this problem, assume that all students with an average of
at leat 80% are considered 'honor' roll' students.'''
def test_honor_roll():
	print("testing honor_roll")

	s1 = s.Student("v00987654", [81, 84, 92])
	s2 = s.Student("v00454333", [65, 70, 81])
	s3 = s.Student("v00123456", [75, 80, 85])
	s4 = s.Student("v00678765", [90, 60, 60])

	list1 = []
	list2 = [s1, s2, s3, s4]

	result = honor_roll(list1)
	print_test("testing with empty list", result==[])

	result = honor_roll(list2)
	expected = [s1, s3]
	print_test("testing with list2", result==expected)
	print()

# ((list of Student) -> (list of Student))
# create and return a new list of Students of only
# students from los with an average grade >= 80%
def honor_roll(los):
	new_list = [] # list of honor roll students seen so far
	for s in los:
		avg = s.get_average()
		if (avg >= 80):
			new_list.append(s)
	return new_list




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
