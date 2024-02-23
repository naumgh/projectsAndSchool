'''	Example created by Kimiya Pahlevan
	for exam prep for CSC 110, at the
	University of Victoria, Fall 2019'''

import Planet as p
tests = 0
passed = 0

def main():
	#test_hottest_planet()
	#test_sort_planets()
	#test_list_to_dict()
	#test_inner_planet()
	#test_melting_point()
	test_correct_info()
	print("TEST RESULTS:", passed, "/", tests)

def test_hottest_planet():
	print('testing hottest_planet')
	list1=[]
	result = hottest_planet(list1)
	print_test('testing with list1', result==("None",0))

	list2=[p.Planet("Mercury", 1, 0, 332, "solid"), \
	       p.Planet("Venus", 2, 0, 847, "solid"), \
	       p.Planet ("Earth", 3, 1, 61, "solid"), \
	       p.Planet("Mars", 4, 2, -67, "solid"), \
	       p.Planet("Jupiter", 5, 63, -234, "gas"), \
	       p.Planet("Saturn", 6, 82, -288, "gas"), \
	       p.Planet("Uranus", 7, 27, -357, "gas"), \
	       p.Planet("Neptune", 8, 13, -353, "gas")]

	result = hottest_planet(list2)
	print_test('testing with list2', result==("Venus",847))


# ((list of planet)-> tuple)
# takes a list of Planets and returns a tuple containing the
# name of the hottest planet and its average temperatue in F
def hottest_planet(list):
	temp = 0
	index = 0
	max_index = 0
	name = 'None'
	if len(list) > 0:
		for p in list:
			if p.get_temp() > temp:
				temp = p.get_temp()
				max_index = index
				name = p.get_name()
			index += 1
		return name,temp
	return name,temp
    





def test_sort_planets():
	print('testing sort_planets')
	list1 = []
	result = sort_planets(list1)
	print_test('testing with list1', result=={})

	list2=[p.Planet("Venus", 2, 0, 847, "solid"), \
			p.Planet("Neptune", 8, 13, -353, "gas"), \
			p.Planet("Saturn", 6, 82, -288, "gas"),  \
			p.Planet ("Earth", 3, 1, 61, "solid"),  \
			p.Planet("Uranus", 7, 27, -357, "gas"), \
			p.Planet("Mars", 4, 2, -67, "solid"),   \
			p.Planet("Jupiter", 5, 63, -234, "gas"), \
			p.Planet("Mercury", 1, 0, 332, "solid")]


	result = sort_planets(list2)
	expected = [p.Planet("Mercury", 1, 0, 332, "solid"),  \
				p.Planet("Venus", 2, 0, 847, "solid"), \
				p.Planet ("Earth", 3, 1, 61, "solid"),  \
				p.Planet("Mars", 4, 2, -67, "solid"),   \
				p.Planet("Jupiter", 5, 63, -234, "gas"), \
				p.Planet("Saturn", 6, 82, -288, "gas"),  \
				p.Planet("Uranus", 7, 27, -357, "gas"), \
				p.Planet("Neptune", 8, 13, -353, "gas")]
	print_test('testing with list2', result==expected)


# (list of Planets) -> (list of Planets)
# takes a list of Planets and returns a list of
# planets sorted from closest to farthest from sun
def sort_planets(list):
    place = 1
    new_list = []
    for x in range(len(list)):
    	for planet in list:
    		if planet.get_place() == place:
    			new_list.append(planet)
    			place += 1
    print(new_list)
    return new_list
    		 





def test_list_to_dict():
	print('testing list_to_dict')
	list1 = []
	result = list_to_dict(list1)
	expected = {}
	print_test("testing with empty list", result == expected)

	list2=[p.Planet("Venus", 2, 0, 847, "solid"), \
			p.Planet("Neptune", 8, 13, -353, "gas"), \
			p.Planet("Saturn", 6, 82, -288, "gas"),  \
			p.Planet ("Earth", 3, 1, 61, "solid"),  \
			p.Planet("Uranus", 7, 27, -357, "gas"), \
			p.Planet("Mars", 4, 2, -67, "solid"),   \
			p.Planet("Jupiter", 5, 63, -234, "gas"), \
			p.Planet("Mercury", 1, 0, 332, "solid")]
	result = list_to_dict(list2)
	expected = {2:"Venus",
				8:"Neptune", 
				6:"Saturn",
				3:"Earth", 
				7:"Uranus",
				4:"Mars",
				5:"Jupiter",
				1:"Mercury"}
	print_test("testing with list2", result == expected)


# (list of Planets) -> dict
# takes a list of Planets and returns a dictionary with
# its placement from the sun as the key and the
# name of the planet as the value

def list_to_dict(lon):
	new_dict = {}
	for planet in lon:
		key = planet.get_place()
		value = planet.get_name()
		new_dict[key] = value
	print(new_dict)
	return new_dict








'''Inner planets are the planets that have a solid
state. Complete the inner_planet method in the Planet
class so that it determines if the given planet is an
inner planet.'''
def test_inner_planet():

	planet1 = p.Planet("Mercury", 1, 0, 332, "solid")
	planet2 = p.Planet("Venus", 2, 0, 847, "solid")
	planet3 = p.Planet("Uranus", 7, 27, -357, "gas")
	planet4 = p.Planet("Neptune", 8, 13, -353, "gas")

	result = planet1.inner_planet()
	print_test('testing with planet1', result==True)

	result = planet3.inner_planet()
	print_test('testing with planet3', result==False)

	result = planet2.inner_planet()
	print_test('testing with planet3', result==True)

	result = planet4.inner_planet()
	print_test('testing with planet3', result==False)








''' Design a function that takes the melting point of
a substance (in Farenheit) and returns the count of
planets in the list that the substance would melt on'''
def test_melting_point():
	planet_list=[p.Planet("Venus", 2, 0, 847, "solid"), \
				p.Planet("Neptune", 8, 13, -353, "gas"), \
				p.Planet("Saturn", 6, 82, -288, "gas"),  \
				p.Planet ("Earth", 3, 1, 61, "solid"),  \
				p.Planet("Uranus", 7, 27, -357, "gas"), \
				p.Planet("Mars", 4, 2, -67, "solid"),   \
				p.Planet("Jupiter", 5, 63, -234, "gas"), \
				p.Planet("Mercury", 1, 0, 332, "solid")]
	oxycodone = 426
	result = melting_point(planet_list,oxycodone)
	expected = 1
	print_test("testing oxycodone and planets", result == expected)

	butane = -140
	result = melting_point(planet_list, butane)
	expected = 4
	print_test("testing butane and planets", result == expected)



def melting_point(lon, substance):
	count = 0
	for planet in lon:
		if int(planet.get_temp()) > substance:
			count += 1
	print(count)
	return count






def test_correct_info():
	dict1={'Mercury':(1, 0, 200, 'solid'), 'Venus':(2, 0, 847, 'solid'), \
	        'Earth':(4, 2, 61, 'solid'), 'Mars':(4, 4, 67, 'gas'), \
	        'Jupiter':(5, 66, -234, 'gas'), 'Saturn':(6, 63, -288, 'gas'), \
	        'Uranus':(9, 27, -350, 'solid'), 'Neptune':(8, 13, -353, 'gas')}

	result = correct_info("planet_info.csv", dict1)
	print_test("testing result", result == True)
	print_test("testing values updated", dict1 == {'Mercury':(1, 0 ,332, 'solid'), \
	                                            'Venus':(2, 0, 847, 'solid'), \
	                                            'Earth':(3, 1, 61, 'solid'), \
	                                            'Mars':(4, 2, -67, 'solid'), \
	                                            'Jupiter':(5, 63, -234, 'gas'), \
	                                            'Saturn':(6, 82, -288, 'gas'), \
	                                            'Uranus':(7, 27, -357, 'gas'), \
	                                            'Neptune':(8, 13, -353, 'gas')})

	result = correct_info("planet_info.csv", dict1)
	print_test("testing result", result == False)


	dict2 = {}
	result = correct_info("planet_info.csv", dict2)
	print_test("testing result", result == True)
	print_test("testing values correct", dict1 == dict2)



# (file , dict) -> bool
# takes a file with correct planet information,
# and dictionary with the same information.
# The function should update the dictionry if
# there any information about a planet is incorrect.
# Returns True if dictionary modified, False otherwise
def correct_info(filename, dict):
	r = 0
	boolean = False
	print("Fix me!")
	try:
		file_handle = open(filename, 'r')

	except FileNotFoundError:
		print("file not FileNotFoundError")

	for line in file_handle:
		line = line.strip('\n')
		line = line.split(',')
		key = line[0]
		value = int(line[1]),int(line[2]),int(line[3]),line[4]
		if len(dict) == r:
			boolean = True
			dict[key] = value
			r += 1
		if dict[key] != value:
			boolean = True
			dict[key] = value
	return boolean
	print(dict)



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
