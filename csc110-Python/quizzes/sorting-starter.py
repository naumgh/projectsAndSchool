
''' Q1: The following list is part way through a Selection Sort
algorithm. First, determine how many iterations have occurred,
and then fill out what the contents of the list would look like
after running through two more iterations.'''

# current list: [1, 2, 3, 8, 6, 4, 5]      How many interations? 3

# list after next iteration: [1, 2, 3, 4, 6, 8, 5]

# list after next iteration: [1, 2, 3, 4, 5, 8, 6]

''' Q2: Complete the implementation of the Bubble Sort algorithm
based on the pseudocode implementation found on Wikipedia:

procedure bubbleSort(A : list of sortable items )
    n = length(A)
    repeat
        swapped = false
        for i = 1 to n-1 inclusive do
            /* if this pair is out of order */
            if A[i-1] > A[i] then
                /* swap them and remember something changed */
                swap( A[i-1], A[i] )
                swapped = true
            end if
        end for
    until not swapped
end procedure '''

# ((list of int) -> None)
# sort the given list using the bubble sort algorithm
def bubble_sort(lon):
	print("sorting:", lon)
	listlen = len(lon)
	swapped == True
	while swapped == True:
		swapped == False
		for i in range(0, listlen-1):
			first_elem = i[0+ i]
			second_elem = i[1 + i]
			if first_elem > second_elem: 
				new_first = first_elem
				second_elem = first_elem
				first_elem = new_first
				swapped == True
			else:
				new_second = second_elem
				first_elem = second_elem
				second_elem = new_second
				swapped == True
	return lon




# ((list of int), int, int -> None)
# swap the element at index i1 with the
# element at index i2 in the given list
def swap(lon, i1, i2):
	print("swapping positions", i1, "and", i2)

def test_swap():
	print("testing swap")
	list1 = [9, 1, 6, 4]
	swap(list1, 0, 2)
	print_test("swapping elements 0 and 2", list1==[6,1,9,4])
	list2 = [6, 9, 1, 3, 5, 7]
	swap(list2, 5, 1)
	print_test("swapping elements 5 and 1", list2==[6,7,1,3,5,9])
	# add more tests..


def test_bubble_sort():
	print("testing bubble_sort")
	list1 = [6, 9, 1, 3, 5, 7]
	bubble_sort(list1)
	print_test("sorting list1", list1==[1, 3, 5, 6, 7, 9])
	list2 = [8, 1, 2, 3, 6, 4, 5]
	bubble_sort(list2)
	print_test("sorting list2", list2==[1,2,3,4,5,6,8])
	# add more tests...

tests = 0
passed = 0

def main():
	test_swap()
	test_bubble_sort()
	print("TEST RESULTS:", passed, "/", tests)

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
