	.include "display.asm"
	.data
	
GEN_A:	.space 256
GEN_B:	.space 256
GEN_Z:	.space 256


# Students may modify the ".data" and "main" section temporarily
# for their testing. However, when evaluating your submission, all
# code from lines 1 to 33 will be replaced by other testing code
# (i.e., we will only keep code from lines 34 onward). If your
# solution breaks because you have ignored this note, then a mark
# of zero for Part 3 of the assignment is possible.

TEST_PATTERN:
	.word   0x0000 0x0000 0x0ff8 0x1004 0x0000 0x0630 0x0000 0x0080
        	0x0080 0x2002 0x1004 0x0808 0x0630 0x01c0 0x0000 0x0000

		
	.text
main:
	
	
	la $a0, GEN_A
	jal draw_16x16
	
	addi $v0, $zero, 10
	syscall
	
	la $a0, GEN_A
	la $a1, TEST_PATTERN
	jal bitmap_to_16x16

			
	

# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

	.data
	
# Available for any extra `.eqv` or data needed for your solution.

	.text
	

# bitmap_to_16x16:
#	
# $a0 is destination 16x16 byte array
# $a1 is the start address of the pattern as encoded in a 16-word
#     sequence of row bitmaps.
#
# $v0 holds the value of the bytes around the row and column
# 
# Please see the assignment description for more
# information regarding the expected behavior of
# this function.

bitmap_to_16x16:
	addi $sp, $sp, -24
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	sw $s2, 12($sp)
	sw $s3, 16($sp)
	sw $s4, 20($sp)
	
	add $s0, $zero, $a0	# $s0 is the 16x16 byte array we're initializing
	add $s4, $zero, $a1	# $s4 is the address of the pattern in memory
	
	add $s1, $zero, $zero	# $s1 is the current row
bitmap_to_16x16_row:
	lw $s3, 0($s4)		# $s3 is the pattern value of the current row
	add $s2, $zero, $zero	# $s2 is the current column
bitmap_to_16x16_column:
	add $a0, $zero, $s0
	add $a1, $zero, $s1	
	add $a2, $zero, $s2
	andi $a3, $s3, 0x01	# take advantage of the fact we store 0 or 1 in 16x16 byte array	
	jal set_16x16
	
	addi $s2, $s2, 1	# next column ...
	srl $s3, $s3, 1		# ... but make sure to advance to next bit in pattern for current row.
	blt $s2, 16, bitmap_to_16x16_column	# I give up. Time to use more pseudo-instructions...
	
	addi $s1, $s1, 1	# next row...
	addi $s4, $s4, 4	# ... and advance to address of next row's pattern
	blt $s1, 16, bitmap_to_16x16_row
	
	
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $s2, 12($sp)
	lw $s3, 16($sp)
	lw $s4, 20($sp)	
	addi $sp, $sp, 24
	jr $ra
	
	
# draw_16x16:
#
# $a0 holds the start address of the 16x16 byte array 
# holding the pattern for the Bitmap Display tool.
#
# Assumption: A value of 0 at a specific row and column means
# the pixel at the row & column in the bitmap display is
# off (i.e., black). A value of 1 at a specific row and column
# means the pixel at the row & column in the bitmap display
# is on (i.e., white). All other values (i.e., 2 and greater)
# are ignored.

draw_16x16:
	addi $sp, $sp, -16
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	sw $s2, 12($sp)
	
	add $s0, $zero, $a0	# $s0 is the location of source 16x16 byte array
	
	add $s1, $zero, $zero	# $s1 is the current row
draw_16x16_row:
	add $s2, $zero, $zero	# $s2 is the current column
draw_16x16_col:
	add $a0, $zero, $s0
	add $a1, $zero, $s1
	add $a2, $zero, $s2
	jal get_16x16

	add $a0, $zero, $s1
	add $a1, $zero, $s2
	sub $a2, $zero, $v0	# Converting 0x01 to 0xffffffff, and leaving 0x0 as 0x00000000
	jal set_pixel

	addi $s2, $s2, 1
	blt $s2, 16, draw_16x16_col
	addi $s1, $s1, 1
	blt $s1, 16, draw_16x16_row
	
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $s2, 12($sp)	
	addi $sp, $sp, 16
	jr $ra


# Use here your solution to Part B for this function
# (i.e., copy-and-paste your code).


# sum_neighbours:
#
# $a0 is 16x16 byte array
# $a1 is row (0 is topmost)
# $a2 is column (0 is leftmost)
#
# $v0 holds the value of the bytes around the row and column
sum_neighbours:
	add $v0, $zero, $zero       #int sum = 0;
	
	addi $t0, $a1, -1           #int start_row = row - 1;
	
	addi $t1, $a2, -1			#int start_col = column - 1;
								
	addi $t2, $a1, 1			#int end_row = row + 1;
								
	addi $t3, $a2, 1			#int end_col = column + 1;
	
	add $t4, $t0, $zero        #initializing int i
	
	add $t5, $t1, $zero        #initializing int j
	
	#flag to determine when to skip
	add $t7, $zero, $zero
	
	for1:
	
		for2:
	 	#determines whether or not we need to skip using a flag
	 	addi $t7, $t7, 1
	    beq $t7, 5, skip_sum
	    
	    #saving all the values necessary to the stack
	    add $sp, $sp, -4	
		sw $t7, 0($sp)
	    add $sp, $sp, -4	
		sw $ra, 0($sp)
	    add $sp, $sp, -4	
		sw $v0, 0($sp)
		add $sp, $sp, -4	
		sw $t0, 0($sp)	
		add $sp, $sp, -4	
		sw $t1, 0($sp)	
		add $sp, $sp, -4	
		sw $t2, 0($sp)	
		add $sp, $sp, -4	
		sw $t3, 0($sp)	
		add $sp, $sp, -4	
		sw $t4, 0($sp)	
		add $sp, $sp, -4	
		sw $t5, 0($sp)	
		add $sp, $sp, -4	
		sw $a0, 0($sp)			
	    add $a1, $t4, $zero
	    add $a2, $t5, $zero
	    jal get_16x16
	    add $t6, $v0, $zero
	    lw $a0, 0($sp)
		add $sp, $sp, 4
	   	lw $t5, 0($sp)
		add $sp, $sp, 4
		lw $t4, 0($sp)
		add $sp, $sp, 4
		lw $t3, 0($sp)
		add $sp, $sp, 4
		lw $t2, 0($sp)
		add $sp, $sp, 4
		lw $t1, 0($sp)
		add $sp, $sp, 4
		lw $t0, 0($sp)
		add $sp, $sp, 4
		lw $v0, 0($sp)
		add $sp, $sp, 4
		lw $ra, 0($sp)
		add $sp, $sp, 4	
		lw $t7, 0($sp)
		add $sp, $sp, 4		
		
		add $v0, $v0, $t6
	   										#fix the stack
		
		
		skip_sum:
	    
	  
		
		addi $t5, $t5, 1			#j++
		ble $t5, $t3, for2 			#j <= end_col
	
	
	
	
	
	
	addi $t4, $t4, 1 			#i++
	addi $t5, $t5, -3 
	addi $a2, $a2, 1
	ble $t4, $t2, for1			#i <= end_row
	
	
	
	
	
	jr $ra
	
	
	
	
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
