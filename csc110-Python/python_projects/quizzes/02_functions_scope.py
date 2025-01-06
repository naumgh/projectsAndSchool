# Q1. Below is some code that calls a function and some that defines that function
# Run this code to see the error message generated and fix the error.

foo()

def foo():
    print('this is my function foo')




# Q2a.  What is the output given the following code?
# Answer on paper before uncommenting and running to check your answers.
# Q2b.  Why does this not generate the error message like we saw in Q1:
#       'NameError: name 'func_2' is not defined'

#def func_1():
#    print('func_1')
#    func_2()
#
#def func_2():
#    print('func_2')
#
#func_1()




# Q3.   Consider the following global variable and function definitions with local variables
# Some of the print statements are acessing variables out of scope.
# Answer questions a and b below to see the implications of local vs global scope

my_global_var = 20

def func_3():
    print('func_3')
    x = 5
    z = 15
    print(x)
    print(y)
    print(z)
    print(my_global_var)

def func_4():
    print('func_4')
    x = 7
    y = 10
    print(x)
    print(y)
    print(z)
    print(my_global_var)
    func_3()

def func_5():
    print('func_5')
    my_global_var = 50

def func_6():
    print('func_6')
    global my_global_var
    my_global_var = 90

# Q3a. If you uncomment and run this code it will generate errors related
#  to access a value outside of the scope it was defined.
# Before running it try to identify which lines will generate the errors.
# Comment out the lines that generate an error one at a time and rerun until there are no errors
#

#func_4()
#print('after call to func_4')
#print(x)
#print(y)
#print(z)
#print(my_global_var)

# Q3b.  What is output of the following code?
# Answer on paper before uncommenting and running to check your answers.
# Are the results what you expected? If not, reason about why the output is generated.

#func_5()
#print('after call to func_5', my_global_var)
#
#func_6()
#print('after call to func_6', my_global_var)




# Q4.  What is the output given the following code?
# Answer on paper before uncommenting and running to check your answers.
def func_1(x):
    print('func_1:', x)
    x += 1
    print('func_1:', x)

def func_2():
    y = 5
    print('func_2:', y)
    func_1(y)
    print('func_2: ', y)

func_2()

# Q5.  What is the output given the following code?
# Answer on paper before uncommenting and running to check your answers.
def func_3(x):
    print('func_3:', x)
    x *= 2
    print('func_3:', x)

def func_4():
    x = 6
    print('func_4:', x)
    func_3(x)
    print('func_4: ', x)

func_4()


# Q6.   Design a function that will print your name and an ascii art image.
#   Looking for inpispiration, check out: https://www.asciiart.eu/animals
# By 'Design' we mean:
#   - define the function WITH documentation add
#   - call the function to test it
# In this course we encourage you to route your test calls through
#   a main function as opposed to making the call at global scope as done in Q1-Q3.
# The main function is then called at global scope usually at the bottom of the file.
# This approach is demonstrated in your labs and assignments.
