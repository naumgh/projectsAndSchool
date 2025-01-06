# UVic CSC 230, Summer 2020
# Assignment #1, part A

# Student name: Keanu Reeves
# Student number: V1234576


# Compute M % N, where M must be in $8, N must be in $9,
# and M % N must be in $15.


.text
start:
	lw $8, testcase4_M
	lw $9, testcase4_N

# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	
	nop
	addi $15, $0, -10

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE

exit:
	add $2, $0, 10
	syscall
		

.data

# testcase1: 370 % 120 = 10
#
testcase1_M:
	.word	370
testcase1_N:
	.word 	120
	
# testcase2: 24156 % 77 = 55
#
testcase2_M:
	.word	24156
testcase2_N:
	.word 	77

# testcase3: 21 % 0 = -1
#
testcase3_M:
	.word	21
testcase3_N:
	.word 	0
	
# testcase4: 33 % 120 = 33
#
testcase4_M:
	.word	33
testcase4_N:
	.word 	120
