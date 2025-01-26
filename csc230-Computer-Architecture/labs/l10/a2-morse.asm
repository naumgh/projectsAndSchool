.text


main:	



# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

	## Test code that calls procedure for part A
	# jal save_our_souls

	## morse_flash test for part B
	# addi $a0, $zero, 0x42   # dot dot dash dot
	# jal morse_flash
	
	## morse_flash test for part B
	# addi $a0, $zero, 0x37   # dash dash dash
	# jal morse_flash
		
	## morse_flash test for part B
	# addi $a0, $zero, 0x32  	# dot dash dot
	# jal morse_flash
			
	## morse_flash test for part B
	# addi $a0, $zero, 0x11   # dash
	# jal morse_flash	
	
	# flash_message test for part C
	# la $a0, test_buffer
	# jal flash_message
	
	# letter_to_code test for part D
	# the letter 'P' is properly encoded as 0x46.
	# addi $a0, $zero, 'P'
	# jal letter_to_code
	
	# letter_to_code test for part D
	# the letter 'A' is properly encoded as 0x21
	# addi $a0, $zero, 'A'
	# jal letter_to_code
	
	# letter_to_code test for part D
	# the space' is properly encoded as 0xff
	# addi $a0, $zero, ' '
	# jal letter_to_code
	
	# encode_message test for part E
	# The outcome of the procedure is here
	# immediately used by flash_message
	la $a0, message02
	la $a1, buffer01
	jal encode_message
	la $a0, buffer01
	jal flash_message
	
	
	# Proper exit from the program.
	addi $v0, $zero, 10
	syscall

	
	
###########
# PROCEDURE
save_our_souls:
	addi $sp, $sp -8    	# Room to save $s0, $ra
	sw $s0, 0($sp)		# "Push" value of $s0
	sw $ra, 4($sp)		# "Push" value of $ra

	addi $s0, $zero, 3
SOS_A:
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_short
	addi $s0, $s0, -1
	bne $s0, $zero, SOS_A
	
	jal delay_long
	
	addi $s0, $zero, 3
SOS_B:
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	addi $s0, $s0, -1
	bne $s0, $zero, SOS_B
	
	addi $s0, $zero, 3
SOS_C:
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_short
	addi $s0, $s0, -1
	bne $s0, $zero, SOS_C
		
	lw $s0, 0($sp)		# Restore original value of $s0
	lw $ra, 4($sp)		# Restore original value of $ra
	addi $sp, $sp, 8	# Shrink stack by two words
	jr $31


# PROCEDURE
morse_flash:
	add $sp, $sp, -16
	sw $ra, 0($sp)
	sw $s0, 4($sp)		# Use $s0 to work with low-nibble (dots, dashes)
	sw $s1, 8($sp)		# Use $s1 to work with high-nibble (# of symbols)
	sw $s2, 12($sp)		# For mask used to isolate bit in dot/dash pattern
	
	# Special case: if the parameter is 0xff, then 
	# We have a "space" (i.e., three delay_long)
	add $t0, $zero, 0xff
	and $t1, $a0, $t0
	bne $t1, $t0, morse_flash_proceed
	jal delay_long
	jal delay_long
	jal delay_long
	beq $zero, $zero, morse_flash_return

morse_flash_proceed:
	add $s0, $zero, $a0
	add $s1, $zero, $a0
		
	andi $s0, $s0, 0x0f	# Mask out low nibble: this is dot/dash pattern
	srl  $s1, $s1, 4        # Shift high nibble: this is length of pattern
	
	addi $s2, $zero, 1	# Create mask we'll need to determine dots, dashes
	add  $t0, $zero, $s1     # Need to shift the bit in mask by ($s1 - 1) positions left
	addi $t0, $t0, -1
	sllv $s2, $s2, $t0
	
	# Main loop: Once per dot/dash symbol in $s0
	# $s1 is the number of symbols (dot/dash) left to process
morse_flash_loop:
	beq $s1, $zero, morse_flash_return	# top of morse_flash_loop
	and $t0, $s0, $s2
	beq $t0, $zero, morse_flash_dot
	
	# If we're here, it is because the symbol is a dash
	jal seven_segment_on	# perform dash flashing
	jal delay_long
	jal seven_segment_off
	jal delay_long
	beq $zero, $zero, morse_flash_advance
	
morse_flash_dot:
	jal seven_segment_on	# perform dot flashing
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
morse_flash_advance:
	srl $s2, $s2, 1		# go to the next symbol
	addi $s1, $s1, -1
	beq $zero, $zero, morse_flash_loop
	
morse_flash_return:
	jal delay_long
	lw $s0, 4($sp)		# return from morse_flash_advance
	lw $s1, 8($sp)
	lw $s2, 12($sp)
	lw $ra, 0($sp)
	add $sp, $sp, 16
	jr $ra

###########
# PROCEDURE
flash_message:
	add $sp, $sp, -12
	sw $ra, 0($sp)
	sw $s0, 4($sp)		# Will hold the current message-byte address
	sw $s1, 8($sp)		# Will hold the current message-byte vallue
	
	add $s0, $zero, $a0
flash_message_loop:
	lb $s1, 0($s0)
	beq $s1, $zero, flash_message_return
	add $a0, $zero, $s1
	jal morse_flash
	addi $s0, $s0, 1
	beq $zero, $zero, flash_message_loop
	
flash_message_return:	
	lw $s1, 8($sp)
	lw $s0, 4($sp)
	lw $ra, 0($sp)
	jr $ra
	
	
###########
# PROCEDURE
letter_to_code:
	add $sp, $sp, -12
	sw $ra, 0($sp)
	sw $s0, 4($sp)		# $s0 will be our letter made into an offset
	sw $s1, 8($sp)		# $s1 will be the address into "codes"
	
	addi $t0, $zero, ' '   # Special case of space
	bne $a0, $t0, letter_to_code_proceed
	addi $v0, $zero, 0xff
	beq $zero, $zero, letter_to_code_return
	
	# The procedure could, of course, proceed in a loop
	# from the start of "codes", examining each
	# entry in turn by comparing the letter to what
	# is in $a0. However, because of the alignment of
	# each entry on an eight-byte boundary, we'll
	# compute the address instead as an offset from
	# the start of "codes". The fewer error-prone loops,
	# the better!
	
letter_to_code_proceed:		# Assuming well-formed input here.
	add $s0, $zero, $a0	# Transform $s0 into an offset where 'A' is zero.
	add $t0, $zero, 'A'
	sub $s0, $s0, $t0
	sll $s0, $s0, 3		# Multiply offset by 8.
	
	la $s1, codes
	add $s1, $s1, $s0
	addi $s1, $s1, 1	# We are now at the first dot/dash
	
	addi $t0, $zero, 1	# $t0 will be our ever-present 0x1 mask
	add $t1, $zero, $zero	# $t1 will hold the dot-dash pattern so far
	add $t2, $zero, $zero	# $t2 will hold	the length of the pattern so far
	addi $t3, $zero, '.'	# $t3 holds '.' to "tidy up" comparisons
				# ... and $t4 will hold the '.' or '-' pattern
				
letter_to_code_loop:
	lb $t4, 0($s1)
	beq $t4, $zero, letter_to_code_finish
	
	sll $t1, $t1, 1
	beq  $t4, $t3, letter_to_code_not_dash	
	or  $t1, $t1, $t0	# Assume that if not dot, then must be a dash
	
letter_to_code_not_dash:
	addi $t2, $t2, 1
	addi $s1, $s1, 1
	beq $zero, $zero, letter_to_code_loop
	
letter_to_code_finish:
	sll $t2, $t2, 4		# shift pattern-length to high nibble
	or $t1, $t1, $t2	# bit-wise OR $t2 into the pattern in low-nibble ($t1)
	add $v0, $zero, $t1	# Ensure result of all this is in return-value register
	
letter_to_code_return:
	lw $s1, 8($sp)
	lw $s0, 4($sp)
	lw $ra, 0($sp)
	add $sp, $sp, 12
	jr $ra	


###########
# PROCEDURE
encode_message:
	add $sp, $sp, -12
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	
	add $s0, $zero, $a0	# Location of message text
	add $s1, $zero, $a1	# Location of destination buffer
	
encode_message_loop:
	lb $t0, 0($s0)
	beq $t0, $zero, encode_message_return
	add $a0, $zero, $t0
	jal letter_to_code
	sb $v0, 0($s1)
	addi $s0, $s0, 1
	addi $s1, $s1, 1
	beq $zero, $zero, encode_message_loop
	
encode_message_return:
	sb $zero, 0($s1)   	# Make sure the null is there!!
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	add $sp, $sp , 12
	
	jr $ra
	

###########
# PROCEDURE
seven_segment_on:
	la $t1, 0xffff0010     # location of bits for right digit
	addi $t2, $zero, 0xff  # All bits in byte are set, turning on all segments
	sb $t2, 0($t1)         # "Make it so!"
	jr $31


###########
# PROCEDURE
seven_segment_off:
	la $t1, 0xffff0010	# location of bits for right digit
	sb $zero, 0($t1)	# All bits in byte are unset, turning off all segments
	jr $31			# "Make it so!"
	

###########
# PROCEDURE
delay_long:
	add $sp, $sp, -4	# Reserve 
	sw $a0, 0($sp)
	addi $a0, $zero, 600
	addi $v0, $zero, 32
	syscall
	lw $a0, 0($sp)
	add $sp, $sp, 4
	jr $31

	
###########
# PROCEDURE			
delay_short:
	add $sp, $sp, -4
	sw $a0, 0($sp)
	addi $a0, $zero, 200
	addi $v0, $zero, 32
	syscall
	lw $a0, 0($sp)
	add $sp, $sp, 4
	jr $31





#############
# DATA MEMORY
.data
codes:
	.byte 'A', '.', '-', 0, 0, 0, 0, 0
	.byte 'B', '-', '.', '.', '.', 0, 0, 0
	.byte 'C', '-', '.', '-', '.', 0, 0, 0
	.byte 'D', '-', '.', '.', 0, 0, 0, 0
	.byte 'E', '.', 0, 0, 0, 0, 0, 0
	.byte 'F', '.', '.', '-', '.', 0, 0, 0
	.byte 'G', '-', '-', '.', 0, 0, 0, 0
	.byte 'H', '.', '.', '.', '.', 0, 0, 0
	.byte 'I', '.', '.', 0, 0, 0, 0, 0
	.byte 'J', '.', '-', '-', '-', 0, 0, 0
	.byte 'K', '-', '.', '-', 0, 0, 0, 0
	.byte 'L', '.', '-', '.', '.', 0, 0, 0
	.byte 'M', '-', '-', 0, 0, 0, 0, 0
	.byte 'N', '-', '.', 0, 0, 0, 0, 0
	.byte 'O', '-', '-', '-', 0, 0, 0, 0
	.byte 'P', '.', '-', '-', '.', 0, 0, 0
	.byte 'Q', '-', '-', '.', '-', 0, 0, 0
	.byte 'R', '.', '-', '.', 0, 0, 0, 0
	.byte 'S', '.', '.', '.', 0, 0, 0, 0
	.byte 'T', '-', 0, 0, 0, 0, 0, 0
	.byte 'U', '.', '.', '-', 0, 0, 0, 0
	.byte 'V', '.', '.', '.', '-', 0, 0, 0
	.byte 'W', '.', '-', '-', 0, 0, 0, 0
	.byte 'X', '-', '.', '.', '-', 0, 0, 0
	.byte 'Y', '-', '.', '-', '-', 0, 0, 0
	.byte 'Z', '-', '-', '.', '.', 0, 0, 0
	
message01:	.asciiz "A A A"
message02:	.asciiz "SOSOSOSOSO"
message03:	.asciiz "WATERLOO"
message04:	.asciiz "DANCING QUEEN"
message05:	.asciiz "CHIQUITITA"
message06:	.asciiz "THE WINNER TAKES IT ALL"
message07:	.asciiz "MAMMA MIA"
message08:	.asciiz "TAKE A CHANCE ON ME"
message09:	.asciiz "KNOWING ME KNOWING YOU"
message10:	.asciiz "FERNANDO"

buffer01:	.space 128
buffer02:	.space 128
test_buffer:	.byte 0x30 0x37 0x30 0x00    # This is SOS
