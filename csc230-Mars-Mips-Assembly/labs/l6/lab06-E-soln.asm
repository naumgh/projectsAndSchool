.data

seven_segment:
	.byte 0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x5f, 0x7c, 0x39, 0x5e, 0x79, 0x71
	
.text
	addi $a0, $zero, 0x2b
	jal count_up_with_display
	jal display_dashes
	
finish:
	addi $v0, $zero, 10
	syscall


# $a0: Maximum counter value

count_up_with_display:
	addi $sp, $sp, 16
	sw $ra, 12($sp)
	sw $s0, 8($sp)
	sw $s1, 4($sp)
	sw $s2, 0($sp)

	add $s0, $zero, $a0	# Keep maximum counter value in $s0
	add $s1, $zero, $zero 	# Current counter value
count_loop:
	addi $s1, $s1, 1
	andi $a0, $s1, 0x0f
	add $a1, $zero, $zero
	jal display_hex_digit
	
	add $a0, $zero, $s1
	srl $a0, $a0, 4
	andi $a0, $a0, 0xf
	add $a1, $zero, 1
	jal display_hex_digit

	jal delay_400_msec

	bne $s1, $s0, count_loop
	
	lw $s2, 0($sp)
	lw $s1, 4($sp)
	lw $s2, 8($sp)
	lw $ra, 12($sp)
	jr $ra


# $a0: hex digit to be displayed
# $a1: 0 == right display; 1 == left display

display_hex_digit:
	addi $sp, $sp -12
	sw $ra, 8($sp)
	sw $s0, 4($sp)
	sw $s1, 0($sp)
	
	la $s0, seven_segment
	add $s0, $s0, $a0
	lb $s1, 0($s0)		# We now have the bit sequence for the digit
	
	la $s0, 0xffff0010
	add $s0, $s0, $a1	# A bit of a trick
	sb $s1, 0($s0)

	
	lw $ra, 8($sp)
	lw $s0, 4($sp)
	lw $s1, 0($sp)
	addi $sp, $sp, 12
	jr $ra
	
	
delay_400_msec:
	addi $sp, $sp -4
	sw $ra, 0($sp)
	
	addi $a0, $zero, 400
	addi $v0, $zero, 32
	syscall
	
	lw $ra, 0($sp)
	add $sp, $sp, 4
	jr $ra
	

display_dashes:
	addi $sp, $sp, -20
	sw $s0, 0($sp)
	sw $s1, 4($sp)
	sw $s2, 8($sp)
	sw $s3, 12($sp)
	sw $ra, 16($sp)
	
	la $s0, 0xffff0011
	la $s1, 0xffff0010

	addi $s2, $zero, 0x40
	addi $s3, $zero, 0x40
	
	sb $s2, 0($s0)
	sb $s3, 0($s1)

	lw $s0, 0($sp)
	lw $s1, 4($sp)
	lw $s2, 8($sp)
	lw $s3, 12($sp)
	lw $ra, 16($sp)
	addi $sp, $sp, 20
	
	jr $ra
	
