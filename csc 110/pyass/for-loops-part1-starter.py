passed = 0
tests = 0
THRESHOLD = 0.1

def main():
    test_squares()
    #test_sum_squares()
    test_tminus()

    print(passed, "/", tests, " tests passed")

'''Q1: Write a function squares which takes a number
and prints out the squares from 1 up to but not
including that number. '''

def test_squares():
    squares(5)

def squares(r):
    suma = 0
    print("testing squares...")
    for num in range(1,r):
        print(num**2, end=" ")
        
    print("done")


'''Q2: Write a function sum_quares which takes a number
and returns the sum of all squares from 1 up to but not
including that number. '''

def test_sum_squares():
    print("testing sum_squares...")

'''Q3: Write a function tminus which takes a number
and prints from that number down to 1 and the prints blastoff!'''

def test_tminus():
    print("testing tminus...")
    print_test("testing t-minus at zero", result == "blastoff")
    resut = tminus(0)
    



def t_minus(n):
    for num in range(n, 0, -1):
        print(num, end=", ")
    print("blastoff")





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
