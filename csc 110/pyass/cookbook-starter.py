tests = 0
passed = 0

def main():
	test_top_3_ingredients()
	test_add_ingredient()
	test_write_cookbook()

def test_top_3_ingredients():
	print("testing top_3_ingredients")

	ingredients = {"cake":["butter", "flour", "suger", "eggs"],
				"ice cream":["milk", "whipping cream", "sugar"],
				"fudge":["chocolate", "butter"]}

	# will need to run progrm and examine output to test:
	top_3_ingredients(ingredients, "cake")
	top_3_ingredients(ingredients, "fudge")
	top_3_ingredients(ingredients, "pie")


# (dict, str -> None):
# print the top 3 ingredients from the ingredients
# list in the given dictionary for the given item
def top_3_ingredients(dict, item):
	print("Top 3 ingredients for", item)
	
	try:
		list = dict[item]
		for i in range(0, 3):
			print(list[i])
		print("")
	except IndexError:
		print(item, "does not have any more ingredients")
		print("")
	except KeyError:
		print(item, "is not in the cookbook.")
		print("")

def test_add_ingredient():
	print("testing add_ingredient")

	ingredients = {"cake":["butter", "flour", "suger", "eggs"], \
					"ice cream":["milk", "whipping cream", "sugar"], \
					"fudge":["chocolate", "butter"]}

	add_ingredient(ingredients, "fudge", "sugar")
	expected = {"cake": ["butter", "flour", "suger", "eggs"], \
				"ice cream": ["milk", "whipping cream", "sugar"], \
				"fudge": ["chocolate", "butter", "sugar"]}
	print_test("added sugar to fudge", ingredients==expected)

	add_ingredient(ingredients, "pie", "sugar")
	expected = {"cake": ["butter", "flour", "suger", "eggs"], \
				"ice cream": ["milk", "whipping cream", "sugar"], \
				"fudge": ["chocolate", "butter", "sugar"], \
				"pie": ["sugar"]}
	print_test("added sugar to pie", ingredients==expected)


# (dict, str, str -> None)
# add the ingredient to the ingredients list
# for the item in the given dictionary
def add_ingredient(dict, item, ingredient):
	print("adding", ingredient, "as an ingredient to", item)
	try:
	
		if item not in dict:
			dict[item] = []
		list = dict[item]
		list.append(ingredient)

		print(dict)
	except KeyError:
			print("there is no key", item)

def test_write_cookbook():
	print("testing write_cookbook")

	ingredients = {"cake":["butter", "flour", "suger", "eggs"],
				"ice cream":["milk", "whipping cream", "sugar"],
				"fudge":["chocolate", "butter"]}
	write_cookbook(ingredients, "recipes.txt")

# (dict, str -> None):
# write the contents of the dictionary to a file
# named filename with the format for each item:
# item1:
# 	- ingredient 1
#   - ingredient 2
#   - ... (for all ingredients)
def write_cookbook(dict, filename):
	file_handle = open(filename, "a")
	for k,v in dict.items():
		file_handle.write(k + ":\n")
		for ingredients in v:
			str = "\t" + ingredients + "\n"
			file_handle.write(str)
		file_handle.write("\n")
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
