THRESHOLD = 0.1
tests = 0
passed = 0

def main():
    test_get_total_characters()
    test_print_boolean_results()
    test_get_logo_price()
    test_enough_money()
    print ("TEST RESULTS:", passed, "/", tests)

''' Q1. Design a function that is given two phrases,
    and returns the total number of characters found
    in both of the phrases. '''

def test_get_total_characters():
    print("testing get_total_characters")

''' Q2. Design a function that consumes 3 boolean expressions,
    and prints out:
     - "Perfect" if all 3 expressions are True
     - "Pass" if at least 1 expression is True
     - or "Fail" if all of the expressions are False
     '''

def test_print_boolean_results():
    print("testing print_boolean_results")

''' Q3. Assume you are designing a function, called get_logo_price,
    for a design company that specializes in fancy logos. The base
    rate for a word is $2.50, but there is an extra $0.25 for each
    letter in a word that has more than 5 letters. So, for example,
    a 6-letter word would be $2.75, and a 10-letter would would
    be $3.75. The function should consume a single word and return
    the price it would cost for the fancy logo.'''

def test_get_logo_price():
    print("testing get_logo_price")


BASE_RATE = 2.50

''' Q4. Now design a function called enough_money that takes 3
    words and an amount of money. The function should determine
    whether the amount of money given is enough to pay for the
    a logo containing all 3 of the words. Use your logo_price
    function to determine the price of each word separately.
    Return True if there is enough money to pay for logos for
    the three words, or False if there is not.'''

def test_enough_money():
    print("testing test_enough_money")

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
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
