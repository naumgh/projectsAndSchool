# Write code in a file named file_reading.py to calculate the number of words and characters in a file passed in as a command line argument.

# As an example, your program should run like this:

#         python3 file_reading.py filename

# Only 1 file name will be passed at the command line.

# Your code should

#  - do error handling, i.e. print an error if filename does not exist or if the file was not passed as an argument
#  - print the answer to the following questions regarding the file being read:

#         1) How many words are there in the file?
#         2) How many characters are there in the file?
#         An example of acceptable output for this program is:
#                   There are 542 words in this file.
#                   There are 2546 characters in this file.

# You can only use the sys library
# You cannot use any additional libraries
import sys
def main():
    if(len(sys.argv) != 2:
        print("you need 2 arguements")
        return 0
    file_name = input("enter name of file")
    try:
        infile = open(file_name, 'r')
    except FileNotFoundError:
        print("incorrect filename")
    finally:
            f.close()
            return 0
    lines = 0
    words = 0
    char = 0
    for line in infile:
        list_words = line.split()
        lines = lines + 1
        words = words + len(list_words)
        char = char + len(line)
    print("there are " + len(words) + " in this file")
    print("there are " + len(char) + " in this file") 
    print(here )


main()
