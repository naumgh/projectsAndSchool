import math
THRESHOLD = 0.1
passed = 0
tests = 0

def main():
    test_get_largest_abs()
    test_get_circle_area()
    test_get_celcius()
    test_get_pay()
    print(passed, '/', tests, ' tests passed')

''' Q1. design a function that takes two numbers and
    returns the one with the largest absolute value.
    There is a built-in abs function: abs(-4) -> 4'''

def test_get_largest_abs():
    print('testing get_largest_abs')
    result = get_largest_abs(4,-9)
    print("testing get_largest_abs", result == 9)
    result = get_largest_abs(6, -2)
    print("testing get_largest_abs", result == 7)
    
#(int, int ->)
#return the largest absolute value of the given number
def get_largest_abs(x, y):
    global tests 
    global passed
    tests += 1
    if (abs(x) >= abs(y)):
        passed += 1
        return abs(x)
    else:
        passed += 1
        return abs(y)



''' Q2. design a function that takes the radius of a
    circle and returns the area of that circle'''
def test_get_circle_area():
    print('testing get_circle_area')
    result = get_circle_area(2)
    print("testing get_circle_area", result == 12.56)

def get_circle_area(r):
    global tests
    tests += 1
    area = 3.14 * r**2
    print(area)
    return area



''' Q3. design a function that takes a valid temperature
    in farenheit (f) and return the temperature in celcius(c)
    NOTE: c is f - 32 then multiplied by 5/9'''
def test_get_celcius():
    print('testing get_celcius')
    result = get_celcius(10)
    print("testing get_celcius", result == -12.22)

def get_celcius(f):
    c = (f - 32) * 5/9
    print(c)
    return ("{:.2f}".format(c))




''' Q4. design a function that takes the number of hours an
    employee worked in a day and their hourly wage and returns
    their total pay. Assume the number of hours will not be < 0
    or >24 and the wage is not negative. For hours worked beyond
    8 in a day, they receive 1.5 their wage for those hours.'''

def test_get_pay():
    print('testing get_pay')



# prints test_name followed by ": passed" if expression evaluates
# to True, or ": failed" if expression evaluates to False
def print_test(test_name, expression):
    global tests
    global passed
    tests += 1
    if(expression):
        print(test_name + ': passed')
        passed += 1
    else:
        print(test_name + ': failed')

# The following code will call your main function
if __name__ == '__main__':
    main()
