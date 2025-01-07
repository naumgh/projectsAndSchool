import Student as s
tests = 0
passed = 0

def main():
	#test_add_grade()
	#test_get_average()
	#test_average_of_student()
	test_honor_roll()

''' Complete the add_grade method in the Student class so that
it adds a grade to the list of grades in a Student object'''
def test_add_grade():
	print("testing add_grade")

	s1 = s.Student("v00123456", [80, 60, 77, 92])
	print(s1)
	old_grades = s1.get_grades()
	print(old_grades)
	s1.add_grade(75)
	new_grades = s1.get_grades()
	print(new_grades)
	print_test("after adding grade checking lentgh", len(new_grades) ==5)
	

''' Complete the get_average method in the Student class so that
it returns the overall average across all grades of a Student object'''
def test_get_average():
	print("testing get_average")

	s3 = s.Student("v00452902", [20, 90, 100, 75])
	print(s3)
	result = s3.get_average()
	expected = 71.25
	print_test("average of student 3's grades is "+str(expected), result == expected)

	s4 = s.Student("v00452092", [5, 5, 5, 5])
	print(s4)
	result = s4.get_average()
	expected = 5
	print_test("average of student 3's grades is "+str(expected), result == expected)




''' Design a function that takes a list of Student objects
and a string representing a student ID as a parameter, and
returns the average grade for that student if a student
with that ID exists in the list. If there is no student with
the given ID, return 0.'''
def test_average_of_student():
	print("testing average_of_student")
	list1 = [s.Student("v00123456", [81, 84, 92]),\
			s.Student("v02090290", [65, 70, 81]),\
			s.Student("v02560090", [75, 80, 85]),\
			s.Student("v02091490", [90, 60, 60]),\
			s.Student("v07777777", [65, 70, 81]),\
			s.Student("v06666666", [75, 80, 85]),\
			s.Student("v05555555", [90, 60, 60])]

	Str_param = "v05555555"
	result = average_of_student(list1, Str_param)
	expected = 70
	print_test("the average of v05555555 is", result == expected)


	Str_param = "v06969696"
	result = average_of_student(list1, Str_param)
	expected = 0
	print_test("the average of v06969696 is", result == expected)

def average_of_student(lon,vnum):
	total_grade=0
	avg_grade = 0
	for x in range(len(lon)):
		for item in lon:
			if vnum == item.get_sid():
				grades = item.get_grades()
		if vnum != item.get_sid():
			return 0
	
	for x in range(len(grades)):
		total_grade += grades[x]

	#avg_grade = total_grade/3
	print("{:3.0f}".format(total_grade/len(grades)))
	return int("{:3.0f}".format(total_grade/len(grades)))






''' Design a function that takes a list of Student objects
and returns a list of the students who are on the 'honor roll'.
For this problem, assume that all students with an average of
at leat 80% are considered 'honor' roll' students.'''
def test_honor_roll():
	print("testing honor_roll")

	s1=s.Student("v00123456", [81, 84, 92])
	s2=s.Student("v02090290", [65, 70, 81])
	s3=s.Student("v02560090", [75, 80, 85])
	s4=s.Student("v02091490", [90, 60, 60])

	list1=[]
	list2=[s1, s2, s3 ,s4]

	result = honor_roll(list1)
	print_test("testing with empty list", result == [])

	result = honor_roll(list2)
	expected = [s1, s3]
	print_test("testing with list 2", result == expected)

def honor_roll(lon):
	pretentious_fucks = []
	if len(lon) > 0:
		for item in lon:
			average = item.get_average() 
			if average >= 80:
				pretentious_fucks.append(item)
	return pretentious_fucks
	print(pretentious_fucks)

			





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
