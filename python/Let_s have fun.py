Acknowledgments
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/



# 1. front_x
# Given a list of strings, use regex to return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

#2. Write a Python program that matches a string that has an a followed by two to three 'b'.

#3. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

#4. Write a Python program to remove everything except alphanumeric characters from a string. No other special characters exist in the string. 

# 5. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


# 6. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

# 7. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

#8. Create a class Student where an object of the Student class contains information about a student's name, country they were born in, and languages they speak. The Student class also keeps track of all unique names of the countries where the students (in the created objects) were born, as well as all unique languages they speak. 

For this, we will use the Google Colab notebooks, one notebook per breakout room. Steps to follow: 
1. Choose one breakout member to sign into their Google account (or create a Google account)

2a. Click on this share link to access the shared Google Drive folder: https://drive.google.com/drive/folders/1kbEvUTAjInNXnDI7BA5UCnYdK9AiJPwm?usp=sharing
2b. Click the down arrow (or right click) on the Shared with Me > breakout folder at the top of the window and click on "Add shortcut to Drive"

3. Once signed in and shared folder setup, go to: https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=GJBs_flRovLc
and create a  new notebook with New Notebook. Save it "breakoutXX" where XX is your breakout room number. The file will receive the .ipynb extension.  This will automatically create a "Colab Notebooks" folder in your Google Drive.

4. Inside the notebook, create the first Code cell to include this code: 
    from google.colab import drive
    drive.mount('/content/gdrive')
  
Press the play button to run the cell.

You will be prompted to visit at URL, retrieve an authorization code and enter it in the box provided and press enter. Do so :).   You will receive a message that "Mounted at /content/gdrive" once it's successful.

5. You are ready to work in the notebook. When attempting to write to a .txt file, use this code: 
    with open("/content/gdrive/My Drive/breakout/breatkoutXX.txt", "a+") as fh:
    	fh.write(---whatever you wish to write but keep it clean everyone ---)

	note that the file you write in is called breakoutXX.txt, where XX is your breakout room #. 

Now, once you wrote your class and got all this setup, there is one more fun step to the exercise:

6.  To have everyone contribute, you can share your notebook!  Click on Share, click on "Change to anyone with the link" and change "Viewer" to "Editor".  Copy the link and share it with your other breakout members in the Chat. 
NOTE: It can take a bit for changes to sync across the different open sessions so your additions/changes may not be visible to everyone immediately.

Everyone in your group should create an instance of Student with their own information. 

You will later be instructed how to process that information. 


   
  

