# UVic CSC 230, Summer 2020
# Assignment #1, part A

# Student name: Naum Hoffman
# Student number: V00927502


# Compute even parity of word that must be in register $8
# Value of even parity (0 or 1) must be in register $15


.text

start:
	lw $8, testcase2  # STUDENTS MAY MODIFY THE TESTCASE GIVEN IN THIS LINE
	
	
# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# purpose of registers:
# $8: initial input value (plus subsequent modifications)
# $9 count for number of bits set
# $10: count for number of bits set 
# $11: result of masking with 0x1

	#01010101110101011101010111010100
	#00000000000000000000000000000001
	
	#00000000000000000000000000000000
	
	#$10 = 2
	
	#0
	
		
		
	add $10, $0, $0
	add $9, $0, 32
	
loop_start:
	beq $9, $0, determine_parity
	andi $11, $8, 0x1
	beq $11, $0, skip_increment
	addi $10, $10, 1
	
skip_increment:
	srl $8, $8, 1
	addi $9, $9, -1
	beq $0, $0, loop_start
	
determine_parity:
	andi $15, $10, 0x1
	

	
	


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE


exit:
	add $2, $0, 10
	syscall
		

.data

testcase1:
	.word	0x00200020    # even parity is 0

testcase2:
	.word 	0x00300020    # even parity is 1
	
testcase3:
	.word  0x1234fedc     # even parity is is 1

