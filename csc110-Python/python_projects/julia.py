# assignment1.py
#
# Student name: Naum Hoffman	
# Student id:  V00927502

grade_units = 0
totalunits = 0

def main():
   	print("Welcome")
   	displayFunc()


def displayFunc():
    print("1. Enter course grade and units.")
    print("2. Show GPA.")
    print("3. Quit.")
    x=int(input("Enter 1, 2 or 3. "))
    if x==1:
    	legal(x)
    elif x == 2:
    	gpa(x)
    elif x== 3:
    	print("goodbye")

    else:
        print("error message")
        return -1

def legal(x):
	global totalunits
	global grade_units
	if x == 1:
		grade = int(input("enter grade "))
		units = int(input("enter units "))
	if 0 <= grade <=4 and 1 <= units <= 5:
		grade_units = grade*units
		totalunits += units
		print(grade_units)
		print(totalunits)
		main()
	else:
		print("error out of range ")

def gpa(y):
	try:
		my_gpa = grade_units/totalunits
		print(my_gpa)
	except ValueError:
		print("totalunits cannot equal 0 ")


if __name__ == '__main__':
	main()