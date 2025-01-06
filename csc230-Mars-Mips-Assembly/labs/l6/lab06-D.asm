.data

seven_segment:
	.byte 0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f, 0x5f, 0x7c, 0x39, 0x5e, 0x79, 0x71
	
.text
	addi $a0, $zero, 0x06
	addi $a1, $zero, 0
	jal display_hex_digit	
	
	
	addi $a0, $zero, 0x5b
	addi $a1, $zero, 1
	jal display_hex_digit
	
finish:
	addi $v0, $zero, 10
	syscall


# $a0: hex digit to be displayed
# $a1: 0 == right display; 1 == left display

display_hex_digit:
	#li, $t1, 1
	beq $a1, 0, right_disp
	beq $a1, 1, left_disp
	
	
	
	right_disp:
		addi $sp, $sp, -4
		sw $s0, 0($sp)
		la $a2, 0xffff0010
		addu  $s0, $s0, $a0
		sb $s0, -16($a2)
		#lw $s0, 0($sp)
		addi $sp, $sp, 4
		jr $ra
		
	
	left_disp:
		addi $sp, $sp, -4
		sw $s1, 0($sp)
		la $a3, 0xffff0011
		addu $s1, $zero, $a0
		sb $s1, 0($a3)
		#lw $ra, 0($sp)
		addi $sp, $sp, 4
		jr $ra
		

	
	
	
	
	
