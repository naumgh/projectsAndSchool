	.data
	
GEN_A:	.space 256
GEN_B:	.space 256
GEN_Z:	.space 256

TEST_A_16x16:
	.byte  	9 3 8 5 7 0 8 3 9 3 4 7 3 5 7 1
       		4 3 2 1 7 8 5 3 7 5 3 6 6 3 1 6
       		7 4 3 1 9 5 4 6 6 3 6 1 6 6 0 7
       		3 8 1 5 0 5 5 0 4 9 2 0 6 2 4 1
       		2 6 5 9 7 2 7 8 4 2 8 0 1 1 0 9
       		5 8 7 1 9 9 7 2 2 3 8 7 2 1 2 4
       		5 6 1 0 8 8 5 7 0 3 4 5 1 4 2 4
       		7 3 6 1 8 5 3 1 4 2 0 0 6 9 7 9
       		0 5 3 4 7 3 8 9 8 5 5 0 2 4 5 5
       		6 6 0 3 8 1 3 2 1 2 5 1 5 0 7 3
       		5 8 8 3 2 7 8 8 5 4 4 4 3 6 3 7
       		4 0 3 0 9 5 7 7 0 4 8 3 0 7 9 0
       		0 6 7 4 9 2 7 0 0 4 9 1 1 9 7 5
       		8 1 2 7 6 1 4 0 3 5 3 8 1 3 3 2
       		2 9 3 7 2 0 3 8 8 3 1 9 8 0 5 8
       		2 9 7 2 1 1 0 7 9 9 9 9 1 4 6 2
	
	.text
main:

# Students may modify this "main" section temporarily for their testing.
# However, when evaluating your submission, all code from lines 1
# to 61 will be replaced by other testing code (i.e., we will only
# keep code from lines 62 onward). If your solution breaks because
# you have ignored this note, then a mark of zero for Part 1
# of the assignment is possible.
	
	
	la $a0, GEN_B
	la $a1, TEST_A_16x16
	jal copy_16x16			# Memory in data area for GEN_B
					# be an exact copy of data area
					# for TEST_A_16x16
		
	

	addi $v0, $zero, 10
	syscall	
	
	la $a0, GEN_A
	addi $a1, $zero, 15
	addi $a2, $zero, 15
	addi $a3, $zero, 0x1
	jal set_16x16			# Test 1b
	
	
	la $a0, GEN_A
	addi $a1, $zero, 0
	addi $a2, $zero, 0
	addi $a3, $zero, 0x1
	jal set_16x16			# Test 1a
	
	
	la $a0, TEST_A_16x16
	addi $a1, $zero, 13
	addi $a2, $zero, 4
	jal get_16x16			# Test 1c; $v0 should be 6
	

	

	

	

# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	
	.data
	
# Available for any extra `.eqv` or data needed for your solution.

	.text
	

# set_16x16:
#	
# $a0 is 16x16 byte array
# $a1 is row (0 is topmost)
# $a2 is column (0 is leftmost)
# $a3 is the value to be stored (i.e., rightmost 8 bits)
# 
# If $a1 or $a2 are outside bounds of array, then
# nothing happens.

set_16x16:	
	bge $a1, 16, end_set
	blt $a1, 0, end_set
	
	bge $a2, 16, end_set
	blt $a2, 0, end_set
	
	
	#this is done to calculate where we are going to put 
	#the value in the array 
	
	#finding row value
	mul  $t5, $a1, 16
	add $t5, $a0, $t5
	
	#adding remaining offset
	add $t5, $t5, $a2
	
		
	#16 should be at offset 255
	
	#storing word to mem
	sb $a3, ($t5)
	
	
	end_set:
		jr $ra
	
	
# get_16x16:
#
# $a0 is 16x16 byte array
# $a1 is row (0 is topmost)
# $a2 is column (0 is leftmost)
# 
# If $a1 or $a2 are outside bounds of array, then
# the value of zero is returned
#
# $v0 holds the value of the byte at that array location
get_16x16:
	bge $a1, 16, end_get
	blt $a1, 0, end_get
	
	bge $a2, 16, end_get
	blt $a2, 0, end_get
	
	
	#finding row value
	mul  $t5, $a1, 16
	add $t5, $a0, $t5
	
	#adding remaining offset
	add $t5, $t5, $a2
	
	lb $v0, ($t5)
	
	jr $ra
	

	end_get:
		add $v0, $zero, $zero
		jr $ra
		

# copy_16x16:
#
# $a0 is the destination 16x16 byte array
# $a1 is the source 16x16 byte array
copy_16x16:
	#our i value adds by one every loop
	add $t0, $zero, $zero
	
	for:
		lb $t1, ($a1)
		sb $t1, ($a0)
		addi $t0, $t0, 1
		addi $a1, $a1, 1
		addi $a0, $a0, 1
		blt $t0, 256, for
	


	jr $ra


	
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE
