
def main():
    print("starting main...")
    test_get_total_fare()
    test_get_falling_distance()
    test_get_change()


'''
 Q1. Write and test a function that takes a number of
    adults, number of children, and number of seniors
    and returns the cost for everyone to ride the bus.
    Assume: number of people is not negative
'''

CHILD_FARE = 1.50
ADULT_FARE = 2.50
SENIOR_FARE = 2.00

def test_get_total_fare():
    print("testing get_total_fare")
    result = get_total_fare(0, 0, 0)
    print("result expected to be 0.00:", result)
    result = get_total_fare(1, 2, 3)
    print("result expected to be 11.50:", result)

def get_total_fare(childern, adults, seniors):
    total_fare = childern * CHILD_FARE
    total_fare += (adults * ADULT_FARE)
    total_fare += (seniors * SENIOR_FARE)
    return total_fare










'''
 Q2. Write a function that takes the amount of time an
    object takes to fall after being dropped in seconds.
    The function calculates the distance the object fell
    where the formula for distance is:
        d = 1/2 gt^2
    where t is the time and
    g is gravitational acceleration is constant at 9.8 m/s^2
'''
GRAV_ACCEL = 9.8

def test_get_falling_distance():
    print("testing get_falling_distance")
    result = get_falling_distance(2)
    print("the result is", result)

def get_falling_distance(t):
    distance = .5 * GRAV_ACCEL * t**2
    return distance















'''
 Q3. Write a function that takes the total amount of
    money paid for the given number of adult, child,
    and senior bus passengers. The function returns the
    amount of change that should be given back to the
    customer after full payment is made.
'''

def test_get_change():
    print("testing get_change")
    change = get_change(5.50, 2, 3, 4)


def get_change(total_money, child, adult, senior):
    cost = get_total_fare(children, adults, senoirs)
    change = paid - cost
    return change















main()
