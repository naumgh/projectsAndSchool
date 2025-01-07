# assignment1.py
#
# Student name: Naum Hoffman	
# Student id:  V00927502

def main():
	print("Welcome")
	print()
	print_logo()
	calc_surface_area()
   
   # You will call your functions here to test them:


# DEFINE your functions after this line:
def print_cat():
	print_spacer()
	print("| /\\_/\\ |")
	print("| >^.^< |")
	print("|  / \\  |")
	print("| (|_|)~|")

def print_toad():	
	print_spacer()
	print("|  @ @  |")
	print("| (---) |")
	print("|( > < )|")
	print("|\"\"   \"\"|")

def print_logo():
	print_toad()
	print_cat()
	print_toad()
	print_cat()
	print_spacer()
	print_spacer()

def print_spacer():
	print("/-------\\")

def calc_surface_area():
	height = 6
	diameter = 5
	pi = 3.14
	circumfrence = 2 * pi * (diameter/2)
	surface_area_of_tops = pi * ((diameter/2)**2) * 2
	cylinder_walls = height * circumfrence
	total_surface = surface_area_of_tops + cylinder_walls
	print("{:.2f}".format(total_surface))

# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
	main()