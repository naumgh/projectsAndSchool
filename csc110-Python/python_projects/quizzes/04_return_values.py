''' Design the functions described below.
    The design of Q1. get_rectangle_area is provided as an example.
    With functions that return a value, use the print_test function
    to provide feedback of the test results at the command line.
    The print_test function is implemented for you at the bottom of this file.
    RECALL: floating point arithmetic can lose precision.
     Use the <THRESHOLD comparison instead of == to compare floating point results
    '''
import math

THRESHOLD = 0.1

def main():
    print('call your test functions from here')
    test_get_rectangle_area()


''' Example function design, get rectangle area:'''
def test_get_rectangle_area():
    result = get_rectangle_area(0,0)
    expected = 0
    print_test("get_rectangle_area", abs(expected-result)<THRESHOLD)

    result = get_rectangle_area(5.6,2.1)
    expected = 5.6*2.1
    print_test("get_rectangle_area", abs(expected-result)<THRESHOLD)

# (float, float -> float)
# calculates and returns the area of a rectangle of dimensions length by width
def get_rectangle_area(length, width):
    area = length * width
    return area

''' Q1. Design a function called print_dog_years that takes a integer that represents a dog’s age in human years and returns the dog's age in dog years.
    NOTE: a dog's age in dog years is seven times the number of human years it has lived.
    '''

''' Q2. Design a function called get_average that takes three floating point numbers and returns the average of the three numbers.
    '''

''' Q3. Design a function called append that takes two phrases and appends them into one new phrase and returns the new phrase with no space between the two phrases joined.
    Example:
        If the phrases are "hello there" and "you" the function should return "hello thereyou"
    '''

''' Q3. Design a function called distance that takes four floating point numbers as arguments that represent 2 points and calculates and returns the distance between the two points.
    The formula for the distance between two points (x1,y1) and (x2,y2) is:
    d = √((x2-x1)^2 + (y2-y1)^2)
    '''

''' Q4. Design a function called get_shipping_cost that takes the weight of the letter in kgs and the length and width of a letter in cm and calculates and returns the cost of shipping that letter. This function must call the get_rectangle_area function.
    The rules for shipping cost calculations are as follows:
        If the letter is not bigger than the maximum area of 282cm^2 and the weight is less than 0.05kg
        it is a standard size letter and should be charged:
            $1.05 for the baserate  +  additional charge on the weight above 0.03kg at a rate of 20 cents per 10 grams
        Otherwise the letter is non-standard and should be charged:
            $1.90 for the baserate + additional charge on the weight above 0.1kg at a rate of 50 cents per 100 grams
        Example:
            If the package is 12 by 10 cm and weighs 0.24 kgs,
            it is a non-standard package and 140 grams over the 0.1kg non-standard weight limit,
            therefore the shipping cost should be:  1.90 + 1.4 * 0.5 =  2.6
    '''




# (str, bool -> None)
# prints test_name followed by "passed" if expression evaluates to True,
# prints test_name followed by "failed" if expression evaluates to False
def print_test(test_name, expression):
    if(expression):
        print(test_name + ": passed")
    else:
        print(test_name + ": failed")


# The following code will call your main function
if __name__ == '__main__':
    main()
