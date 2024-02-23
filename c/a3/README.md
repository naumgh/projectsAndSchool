TO RUN AND COMPILE: 

javac main.java
java CreateMatrices

this program uses thread pools to multiply two matrices (B X A) and (A X C). Covers all possible

multiplyable cases, and creates random matrices. Result of matrix will then be (B X C). This is 

because the requirement for 2 multiple matrices is:

The first matrix must have the same number of columns as the second matrix has rows

some things to know for testing purposes....

If you want to change maximum cell count, change max in main().
if you want to change max number in cell, change max in ret matrices().

If you want to see the threads printed out (commented out of readibility puroposes), uncomment

line in multiply() the print statement.

 
