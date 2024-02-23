# Q1.   What is the output given the following statements?
# Answer on paper before uncommenting and running to check your answers.
# If there is a sytax error in the line, mark it as invalid on your paper.
#  Comment out the invalid lines to allow all of the remaining code
#  to run when you check your answer.

#print('Welcome to CPSC 110')
#print('Welcome' + 'to' + 'CPSC' + '110')
#print('Welcome' + 'to' + 'CPSC' + 110)
#print('Welcome','to', 'CPSC', '110')
#print('Welcome','to', 'CPSC', 110 )

# Q2.  What is the output given the following statements?
# Answer on paper before uncommenting and running to check your answers.
a = 2.1
b = 2
c = 5
b = 3

#print(a,b,c)
#print(a+b+c)
#print(a)
#print(b)
#print(c)
#
#c = a + b
#print(a,b,c)
#
#b = b * 2
#print(b)
#
#b = b * c
#print(b,c)



# Q3.  Using the variables a, b and c below,
# write assignment statements that will do the following:
# - assign the value of a + 2 to b
# - multiply a and b and store the result to c
# - subtract b from c and store the result to b
# TEST your solution
# add a print statement after each assignment to print the new assigned value
a = 2.1
b = 2
c = 5



# Q4.   Write Python statements that do the following:
# - assigns the sum of 8 and 13 to a variable named total
# - assigns the value 2 to a variable name coupon
# - prints the values of total and coupon
# - multiplies the value of total by .85 and assigns the value to total
# - prints the value of total
# - subtracts the value of coupon from total and assigns the value to total
# - prints the values of total and coupon
# - add the words 'total:' and 'coupon:' to the last print statement




# Q5.   What is the output given the following statements?
# Answer on paper before uncommenting and running to check your answers.
# If there is a sytax error in the line, mark it as invalid on your paper.
#  Comment out the invalid lines to allow all of the remaining code
#  to run when you check your answer.

a = 2.1
b = 2
c = 5
d = 'boo'

#print(a + b)
#print(b + d)
#print(c / b)
#print(b * d)
#print(b // c)
#print(a * b)
#print(a ** b)
#print(c ** b)
#print(d ** b)
#print(d * b)
#print(3 * 3 + 8 / 2)
#print(3 * (3 + 8) / 2)
#print(3 * (3 + 8) // 2)
#print(a + a * c ** b + c // 3)





# Q5a   What is the output of the following code?
# Answer on paper before uncommenting and running to check your answers.
# Q5b   Update this code so it prints WITHOUT changing the function definitions:
#   hi
#   hi
#   there
# HINT: you will want to change the function calls

def my_function1():
    print('hi')

def my_function2():
    print('there')

my_function2()
my_function1()

# Q6a.  What is the output of the following code?
# Answer on paper before uncommenting the call to calc_charge
# and running to check your answers.
# Notice: the calc_charge function does not run without code added to call it
# Q6b.  Update the calc_charge so it prints a $ and the charge with 2 significant figures

TAX = 0.15
def calc_charge():
    print('calc_charge function')
    price = 10
    charge = TAX * price
    print('The charge is', charge, sep=':')

calc_charge()

# Q7.   What is the output given the following statements.
# Answer on paper before uncommenting and running to check your answers.

#x = 39/16
#print('Value of x', format(x, '10f'), sep=':')
#print('Value of x', format(x, '8f'), sep=':')
#print('Value of x', format(x, '2f'), sep=':')
#print('Value of x', format(x, '5.1f'), sep=':')
#print('Value of x', format(x, '5.2f'), sep=':')
#print('Value of x', format(x, '5.3f'), sep=':')

#x = 8
#y = 9
#print('x is', x)
#print('y is', y )

#print('x is', x, end='')
#print('y is', y )

#print('x is', x, end=':')
#print('y is', y )

#print('x is', x, end=' ')
#print('y is', y )


