tests = 0
passed = 0
THRESHOLD = 0.1

def main():
	file_handle = get_file()
	contacts = make_dict(file_handle)
	print(contacts)
	print_dict(contacts)
	test_update_email()
	test_count_between_years()
	test_average_rating()
	print("TEST RESULTS:", tests, "/", passed)

# (None -> file)
# prompt the user to enter a file until a file is found
# return a file object linked to that file for reading
def get_file():
	valid_entry = False
	while (valid_entry == False):
		try:
			file_name = input("Enter file name: ")
			data_file = open(file_name, "r")
			valid_entry = True
		except FileNotFoundError:
			print("Could not read from a file with that name")
	return data_file

# (file -> dict)
# return a dictionary with elements of the form {name: email}
# read in from the given file object
def make_dict(contacts_file):
	contacts = {}
	for k in contacts_file:
		list = k.split()
		contacts[list[0]] = [list[1]]

	return contacts

# (dict -> None)
# prints the contents of the given dictionary,
# each key and value side by side per line
def print_dict(dict):
	for k in dict:
		print('name', k, "email:", dict[k], sep='')


def test_update_email():
	print("testing update email")
	dict = {"Tom":"tom@uvic.ca", "Sam":"sammy@gmail.com",
			"Laura":"lolo@yahoo.ca", "Kim":"kim02@hotmail.com"}

	update_email(dict, "Sam", "sam@gmail.com")
	expected = {"Tom":"tom@uvic.ca", "Sam":"sam@gmail.com",
			"Laura":"lolo@yahoo.ca", "Kim":"kim02@hotmail.com"}
	print_test("Testing by updating Sam's email", dict==expected)

	update_email(dict, "Ann", "Ann@gmail.com")
	expected = {"Tom":"tom@uvic.ca", "Sam":"sam@gmail.com",
			"Laura":"lolo@yahoo.ca", "Kim":"kim02@hotmail.com",
			"Ann":"Ann@gmail.com"}
	print_test("Testing by adding new info for Ann", dict==expected)

# (dict, str, str -> None)
# update the given dictionary by either changing the value for
# the given key if there is an item with the given key; otherwise
# add a new item to the dictionary with given key and value pair
def update_email(dict, name, new_email):
	if name in dict:
		print("updating entry for", name)
	else:
		print("creating a new element")
	dict[name] = new_email







def test_count_between_years():
	print("testing count_between_years")

	movies = {}
	result = count_between_years(movies, 2004, 2008)
	print_test("testing empty dict with 2004, 2008", result==0)

	movies = { "Avengers":(2012, "Fantasy", 7.8),
				"Joker":(2019, "Thriller", 9.1),
				"Titanic":(1997, "Drama", 9.5),
				"Avatar":(2009, "Fantasy", 8.3),
				"Frozen":(2013, "Family", 9.9)}
	result = count_between_years(movies, 2009, 2013)
	print_test("testing movies with 2009, 2013", result==3)
	result = count_between_years(movies, 2010, 2013)
	print_test("testing movies with 2010, 2013", result==2)
	result = count_between_years(movies, 2010, 2012)
	print_test("testing movies with 2010, 2012", result==1)

# (dict, int, int -> int)
# return a count of the number of movies found in the dictionary
# released between min_year and max_year (inclusive)
# dictionary has form {title: (year, genre, rating)}
def count_between_years(dict, min_year, max_year):
	count = 0 
	for i in dict.values():
		year = i[0]
		if min_year <= year <= max_year:
			count += 1




	return count
	print("FIX ME")

def test_average_rating():
	print("testing average_rating")

	movies = {}
	result = average_rating(movies)
	print_test("testing average_rating", result==0)

	movies1 = { "Avengers":(2012, "Fantasy", 7.8),
				"Frozen":(2013, "Family", 9.9)}
	result = average_rating(movies1)
	expected = (9.9+7.8)/2
	print_test("testing movies1", abs(result-expected)<THRESHOLD)

	movies2 = { "Avengers":(2012, "Fantasy", 7.8),
				"Joker":(2019, "Thriller", 9.1),
				"Titanic":(1997, "Drama", 9.5),
				"Avatar":(2009, "Fantasy", 8.3),
				"Frozen":(2013, "Family", 9.9)}
	result = average_rating(movies2)
	expected = (7.8+9.1+9.5+8.3+9.9)/5
	print_test("testing movies2", abs(result-expected)<THRESHOLD)

# (dict -> float)
# return the sum of all movie ratings in the given dictionary
# dictionary has form {title: (year, genre, rating)}
def average_rating(movies):
	sum = 0
	count = 0
	if(len(movies) == 0):
		return 0
	for i in movies.values():
		ratings = i[2]
		count += 1
		sum += ratings
	print(sum/count)
	return sum/count

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
