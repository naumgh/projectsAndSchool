# assignment2.py
# Student name: Naum Hoffman 
# Student id:  V00927502

#calls all the functions required for this assignment 
def main():
    print('Assignment 2')
    test_print_dog_years()
    test_print_area()
    test_print_average()
    test_small_enough_word()
    test_print_max()
    test_print_num_odd()


#calls function print_dog_years, and sets the variable age to an intiger
def test_print_dog_years():
    print_dog_years(0)  # expects 0
    print_dog_years(3)  # expects 21
    print_dog_years(8)  # expects 56

# (int -> None)
# prints the given human age in dog years
def print_dog_years(age):
    print("The dog's age is",age * 7,"in dog years.")


#sets two floats, and calls print_area
def test_print_area():
   print_area(0, 0)       # expects 0.00
   print_area(2.22, 1.23) #expects 2.73

#(float 1, float 2 -> None)
#finds the area of the rectangle with 2 decimal places of precision  
def print_area(length, width):
    area = length * width
    print("the area of the rectangle is", "{:.2F}".format(area))

#sets 3 floats, and calls print_average
def test_print_average():
    print_average(0.0, 0.0, 0.0) #expects 0
    print_average(3.3, 9.9, 29.0) #expects 14.9
    print_average(2.1, 5.6, 3.8) #expects 3.8                          

#(float 1, float 2, float 3)    
#finds the average of 3 numbers with 1 decimal place of precision
def print_average(num1, num2, num3):
    average = (num1 + num2 + num3)/3
    print("the average is:","{:.1F}".format(average))


#calls small_enough_word with a string and intiger as parameters
def test_small_enough_word():
    small_enough_word("anthony", 5) # expects: "Error: anthony is 2 characters too large"
    small_enough_word("Naum", 4) # expects: "Naum is perfectly valid"
    small_enough_word("orange", 3) # expects: "Error: orange is 3 characters too large"
    
#(String, Char -> None)
#finds out how many more characters large a string is in comparison to a int.
def small_enough_word(name, chars):
    word_test = len(name)             #(str -> int)
    how_much_more = word_test - chars
    if(word_test > chars):
      print("Error:",name,"is", how_much_more, "characters too large")
    else:
      print(name, "is perfectly valid")

#calls print_max with 3 different ints as parameters
def test_print_max():
    print_max(0,0,0)  # expects 0
    print_max(3,6,1)  # expects 6
    print_max(1,2,3)  # expects 3
    print_max(8,7,6)  # expects 8

#(int 1, int 2, int 3 -> None)
#prints the max intiger from a group of 3
def print_max(int1, int2, int3):
    if(int1 > int2):
      if(int1 > int3):
        print(int1, "is the max")
    elif(int2 > int3):
      print(int2, "is the max")
    else:
      print(int3, "is the max")

#calls print_num_odd with 3 different intigers as parameters
def test_print_num_odd():
    print_num_odd(0,0,0) #expects "0 odd numbers were found"
    print_num_odd(4,3,1) #expects "2 odd numbers were found"
    print_num_odd(6,9,4) #expects "1 odd numbers were found"

#(int 1, int 2, int 3 -> None)
#counts the amount of odd numbers found in a group of 3 numbers
def print_num_odd(int1, int2, int3):
    total_odd_numbers = 0
    if(int1 % 2 == 1):
      total_odd_numbers += 1
    if(int2 % 2 == 1):
      total_odd_numbers += 1
    if(int3 % 2 == 1):
      total_odd_numbers += 1
    print(total_odd_numbers, "odd numbers were found.")

# The following code will call your main function
# It also allows our grading script to call your main
# DO NOT ADD OR CHANGE ANYTHING PAST THIS LINE
# DOING SO WILL RESULT IN A ZERO GRADE
if __name__ == '__main__':
    main()
