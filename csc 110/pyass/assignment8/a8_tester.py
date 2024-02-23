from assignment8_soln import *

# (str, str, int -> None)
# performs a word frequency analysis on file named filename; writes the
# <num> most frequent words found to a file called top_40_analysis.txt
def analyze_text_file(filename, search_word, num):
	dict = frequency_dictionary(filename)
	if (len(dict) == 0):
		print("Make sure you have downloaded the text files from Connex")
		return
	print("Determining how often", search_word, "occurred in", filename)
	freq = frequency_percentage(dict, search_word)
	freq = format(freq*100, ".2f")
	print("It made up", freq, "%", "of all words")

	list = dict_to_list(dict)
	selection_sort(list)
	write_most_frequent("top_40_analysis.txt", list, num, filename)

# (None -> None)
# sets up the word frequency analysis report by getting input from the user
def top_40_analysis():
	num = 10
	try:
		word = input("What word would you like to search for? ")
		num = int(input("How many words would you like included in the report? "))
	except ValueError:
		print("Invalid value entered, defaulting to 10")

	analyze_text_file("1999.txt", word, num)
	analyze_text_file("2009.txt", word, num)
	analyze_text_file("2019.txt", word, num)

	print("\nOpen top_40_analysis.txt to see the results!")
	print("You can now do analysis of other files as well")

def main():
	top_40_analysis()

main()
