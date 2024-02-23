from assignment7 import *

# (None -> (list of str))
# creates, populates, and returns the list of mutations
# by reading data from the file specified by the user
def file_init():
	data_file = get_file()
	data_list = make_list(data_file)
	print("The file has", len(data_list),"words in it")
	data_file.close()
	return data_list

# ((list of str) -> None)
# searches through the given list and prints out the
# total number of mutations and the longest mutated sequence
def mutation_analysis(data_list):
	total_muts = count_total_mutations(data_list)
	longest = find_longest(data_list)
	print("Total mutations found:", total_muts)
	print("The longest is:", longest)

# ((list of str) -> None)
# prints out the number of times a given sequence is
# found in the given list, both with and without mutations
def frequency_analysis(data_list):
	to_find = input("\nWhat sequence would you like to search for? ")
	freq = get_frequency(data_list, to_find)
	freq_mutations = frequency_incl_mutations(data_list, to_find)
	print("Number of times", to_find, "was found in data set:", freq)
	print("The number of times found, including mutations", freq_mutations)

def main():
	data_list = file_init()
	mutation_analysis(data_list)
	frequency_analysis(data_list)

main()
