# ((list of int) -> float)
# returns the average size of all strings
# found in the given list of strings
def get_average(los):
	if (len(los) == 0):
		return 0.0
	sum = 0 # sum of all string lengths seen so far
	for s in los:
		sum += len(s)
	return sum / len(los)

# (file -> (list of str))
# create and return a new list containing
# all the words found in the file
def get_list(file):
	lista = []
	for x in file:
		print(x)
		lista += x.split()
		print("lista is now", lista)
		print()



def main():
	file_handle = open("words.txt", "r")
	los = get_list(file_handle)
	avg = get_average(los)
	print("Average word length:", avg)

main()
