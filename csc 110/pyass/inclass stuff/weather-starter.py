
tests = 0
passed = 0
THRESHOLD = 0.1

def main():
	test_make_weather_dict()
	# test_count_rainy()
	# test_get_name_hottest()
	dict = make_avg_dict("raw_temps.csv")
	write_csv(dict, "output.csv")
	print("TEST RESULTS:", passed, "/", tests)

def test_make_weather_dict():
	print("testing make_weather_dict")
	dict = make_weather_dict("invalid_name")
	print_test("testing with invalid file", dict=={})

	dict = make_weather_dict("incorrect_format.csv")
	expected = {"January":(4.3, 118), "March":(6.8,55)}
	print_test("testing with invalid file", dict==expected)

	dict = make_weather_dict("victoria-temperature.csv")
	expected = {'January': (4.3, 118), 'February': (5.6, 80),
	'March': (6.8, 55), 'April': (8.8, 38), 'May': (11.6, 26),
	'June': (13.7, 22), 'July': (15.5, 17), 'August': (15.6, 22),
	'September': (13.9, 35), 'October': (10.2, 72),
	'November': (6.9, 112), 'December': (4.9, 121)}
	print_test("testing with 'victoria-temperatute.csv'", dict==expected)

# (str -> dict)
# read the contents of a file with the given name that contains
# comma-separated weather data; create and return a new dictionary
# with the form {str:(float,int)} where each item represents a month
# name, its average temperature in Celsius, and its average preciptation
# in mm. Each line in the input file should be formated with:
# month_name, temp, precipitation
# Skip any lines in file that are formatted incorrectly.
def make_weather_dict(filename):
	new_dict = {}
	try:
		file_handle = open(filename, 'r')
	except FileNotFoundError:
		print("could not find file")
		return new_dict
	for line in file_handle:
		line = line.rstrip()
		list = line.split(",")
		print(list)
		if len(list) == 3:
			key = list[0]
			try:
				temperature = float(list[1])
				precipitation = int(list[2])
				value = (temperature, precipitation) 
				new_dict[key] = value
			except ValueError:
				print("could not convert to numerical value")
		else:
			print("formatted incorrectly")

	return new_dict


def test_count_rainy():
	print("testing count_rainy")
	dict1 = {}
	dict2 = {"January":(4.3, 118), "March":(6.8,55), "August":(15.5,22)}
	dict3 = make_weather_dict("victoria-temperature.csv")

	result = count_rainy(dict1)
	print_test("testing with empty dictionary", result==0)
	result = count_rainy(dict2)
	print_test("testing with only Jan, March, Aug", result==2)
	result = count_rainy(dict3)
	print_test("testing with year-round Victoria data", result==6)

# (dict -> int)
# return a count of the number of months that have at least
# 50mm of precipitation; the dictionary has form {str:(float, int)}
# where the string is month name, and the tuple value contains the
# average temperate in Celsius and precipitation in mm
def count_rainy(dict):
	count = 0
	return count

def test_get_name_hottest():
	print("testing get_name_hottest")
	dict1 = {}
	dict2 = {"January":(4.3, 118), "March":(6.8,55), "October":(10.2,72)}
	dict3 = make_weather_dict("victoria-temperature.csv")

	result = get_name_hottest(dict1)
	print_test("testing with empty dictionary", result=="")
	result = get_name_hottest(dict2)
	print_test("testing with Jan, March, Oct", result=="October")
	result = get_name_hottest(dict3)
	print_test("testing with year-round Victoria data", result=="August")

# (dict -> int)
# return the name of the month found in the dictionary with the
# highest average temperature; the dictionary has form {str:(float, int)}
# where the string is month name, and the tuple value contains the
# average temperate in Celsius and precipitation in mm
def get_name_hottest(dict):
	if (len(dict) == 0):
		return ""


# (str -> dict)
# read the contents of a file with the given name that contains
# comma-separated weather data; each line begins with a month name,
# followed by a random sampling of temperature data; the dictionary
# created and returned should have the form {str:str} where the key
# is the month name, and the value is the average temperature for
# that month read from the input file, formatted to 1 decimal place
def make_avg_dict(filename):
	new_dict = {}
	try:
		file_handle = open(filename, 'r')
		for line in file_handle:
			line = line.rstrip()
			list = line.split(",")
			key = list[0]
			sum = 0
			count = 0
			for q in list[1:]:
				sum += float(q)
				count += 1
			avg = sum/count
			value = format(avg, ".1f")
			new_dict[key] = value
			#(key, val) = x.split()
			#new_dict[int(key)] = val
	except FileNotFoundError:
		print("could not read file")
		return {}
	print(new_dict)
	return new_dict

# (dict -> str)
# write the contents of the dictionary to a file with
# the given file name. Each key-value pair should be
# written on a line separated by a comma
def write_csv(dict, filename):
	try:
		file_handle = open(file_name, 'w')
	except:
		print("file not found")
	for key, value in dict.items():
		string1 = k + ","+v+"\n"
		file_handle.write(string1)
	file_handle.close()

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
