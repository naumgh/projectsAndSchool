.text


main:	



# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

	## Test code that calls procedure for part A
	#jal save_our_souls

	## morse_flash test for part B
	  #addi $a0, $zero, 0x42   # dot dot dash dot
	 # jal morse_flash
	
	## morse_flash test for part B
	#addi $a0, $zero, 0x37   # dash dash dash
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
	addi $a0, $zero, 'P'
	jal letter_to_code
	
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
	# la $a0, message01
	# la $a1, buffer01
	# jal encode_message
	# la $a0, buffer01
	# jal flash_message
	
	
	# Proper exit from the program.
	addi $v0, $zero, 10
	syscall

	
	
###########
# PROCEDURE
save_our_souls:
					#the jumps reqired to get S0S
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_short
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_short
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_short
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_short
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	
	
	
	jr $31


# PROCEDURE
morse_flash:
	move $s0, $ra       #saving return address
			
							#high nib, max_num
					#counter var
	
	andi $t3, $a0, 0x0F           #bitwise and operation, masking out high nibble, so low nibble
					#is left 

	
	srl $t2, $a0, 4			#shifting high nibble to low nibble spot
	
	beq $t2, 4, case_four
	
	beq $t2, 3, case_three
	
	beq $t2, 2, case_two
	
	beq $t2, 1, case_one
	
	case_four:
		srl $t4, $t3, 3
		beqz $t4, case_zero
		jal seven_segment_on
		jal delay_long
		jal seven_segment_off
		jal delay_long
		j case_three
		
		
		
		case_zero:
			jal seven_segment_on
			jal delay_short
			jal seven_segment_off
			jal delay_long
		
			
			
		
	
	case_three:
		andi $t4, $t3, 4
		srl $t4, $t4, 2
		beqz $t4, case_zero1
		jal seven_segment_on
		jal delay_long
		jal seven_segment_off
		jal delay_long
		j case_two
		
		case_zero1:
			jal seven_segment_on
			jal delay_short
			jal seven_segment_off
			jal delay_long
		
	case_two:
		andi $t4, $t3, 2
		srl $t4, $t4, 1
		beqz $t4, case_zero2
		jal seven_segment_on
		jal delay_long
		jal seven_segment_off
		jal delay_long
		j case_one
		
		case_zero2:
			jal seven_segment_on
			jal delay_short
			jal seven_segment_off
			jal delay_long
	
	case_one:
		andi $t4, $t3, 1
		beqz $t4, case_zero3
		jal seven_segment_on
		jal delay_long
		jal seven_segment_off
		jal delay_long 
		jr $s0
		
		case_zero3:
			jal seven_segment_on
			jal delay_short
			jal seven_segment_off
			jal delay_long
		
	jr $s0
###########
# PROCEDURE
flash_message:
	# saving starting address
	move $s0, $a0     
	
	# pushing ra onto stack
	add $sp, $sp, -4	
	sw $ra, 0($sp)	
	flash_message_while_start:
		lb $a0, 0($s0)
		beqz $a0, flash_message_end
				
		# pushing s0 onto stack
		add $sp, $sp, -4	
		sw $s0, 0($sp)	
	
		jal morse_flash
	
		# pop s0 off stack
		lw $s0, 0($sp)
		add $sp, $sp, 4
		
		#add 1 to memory address to read next character
		add $s0, $s0, 1
		
		j flash_message_while_start
	
	
	
	
		
	flash_message_end: 
		# pop ra off stack
		lw $ra, 0($sp)
		add $sp, $sp, 4
		
		jr $ra
	
	
###########
# PROCEDURE
letter_to_code:
	
	#store the starting address of our alphabet array into s2.
	la $s2, codes
	
	#store the input letter into s1.
	lb $s2, 0($a0)
	
	#subtracting the ascii value of letter A from our letter to use as our offset. A will give us zero, 
	#Z will give us 25
	sub $s1, $t7, 'A'
	
	#we stored our offset into s3
	mul $s3, $s1, 8
	
	
	#we are going to iterate through each letter until we find the correct letter, otherwise there 
	#is a problem
	letter_to_code_for_loop_start:
		beqz $s0, if_byte_zero
		if_byte_zero:
			jr $ra
			
	
	jr $ra	


###########
# PROCEDURE
encode_message:
	jr $ra

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE

#############################################
# DO NOT MODIFY ANY OF THE CODE / LINES BELOW

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
message02:	.asciiz "SOS"
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
