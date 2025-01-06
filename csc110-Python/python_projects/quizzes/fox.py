# fox.py
#
# Student name:Naum Hoffman
# Student id:  V00927502

def main():
	fox_says()

# (str -> str)
# prompts the user to enter a phrase and returns the
# user's response; continually asks the user to input
# something until at least 1 character is entered
def get_fox_says(question):
	# TODO: fix this function (and erase this comment)
    x = input(question)
    while(x == ""):
        x = input(question)
    return x

# (str -> None)
# print out the top/bottom edge of quotation box
# based on the size of the given phrase
def print_quotation_edge(size):
	# TODO: fix this function (and erase this comment)
    
    x = len(size)
    for i in range(0, x+4):
        
        print("*",end ='')
    print("")
    

###########################################################
###  YOU DO NOT NEED TO MODIFY ANYTHING BELOW THIS LINE ###
### BUT READING THE CODE IS GOOD FOR CODE UNDERSTANDING ###
###########################################################

# (str -> None)
# prints out a quotation box with quote inside it
def print_quotation_box(quote):
    print_quotation_edge(quote)
    print("|",quote,"|")
    print_quotation_edge(quote)

# (None -> None)
# prints an ASCII fox
def print_fox():
    print("      \\")
    print("       \\ /\\   /\\")
    print("  ____  //\\\\_//\\\\")
    print(" /   /  \\_     _/")
    print("[^^^]    / * * \\")
    print("[   ]    \_\\o/_/")
    print("\\   ]    _/   \\")
    print(" \\  \\  _/     /")
    print("  \\_ \\/  \\ ] ]")
    print("    \\_\\  / ] ]_")

# (None -> None)
# gets input from the user and then places the input text
# into the correct sized quotation box and prints out a fox
def fox_says():
    question = "What does the fox say? "
    quote = get_fox_says(question)
    print_quotation_box(quote)
    print_fox()


# The following code will call your main function
if __name__ == '__main__':
	main()
