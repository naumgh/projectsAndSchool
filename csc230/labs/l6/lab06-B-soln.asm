.text
	addi $s0, $zero, 5
loop:
	beq $s0, $zero, finish
	
	jal display_dashes
	jal delay_400_msec

	jal display_blanks
	jal delay_400_msec
	
	jal display_digits_21
	jal delay_400_msec
	
	jal display_blanks
	jal delay_400_msec
	
	addi $s0, $s0, -1
	
	beq $zero, $zero, loop
	
finish:
	addi $v0, $zero, 10
	syscall
	
	
display_dashes:
	addi $sp, $sp, -16
	sw $s0, 0($sp)
	sw $s1, 4($sp)
	sw $s2, 8($sp)
	sw $s3, 12($sp)
	
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
	
	addi $sp, $sp, 16
	
	jr $ra
	
	
display_blanks:
	addi $sp, $sp, -8
	sw $s0, 0($sp)
	sw $s1, 4($sp)
	
	la $s0, 0xffff0011
	la $s1, 0xffff0010

	sb $zero, 0($s0)
	sb $zero, 0($s1)
	
	lw $s0, 0($sp)
	lw $s1, 4($sp)
	addi $sp, $sp, 8
	
	jr $ra
	
		
display_digits_21:
	addi $sp, $sp, -16
	sw $s0, 0($sp)
	sw $s1, 4($sp)
	sw $s2, 8($sp)
	sw $s3, 12($sp)
	
	la $s0, 0xffff0011
	la $s1, 0xffff0010

	addi $s2, $zero, 0x5b
	addi $s3, $zero, 0x06
	
	sb $s2, 0($s0)
	sb $s3, 0($s1)
	
	lw $s0, 0($sp)
	lw $s1, 4($sp)
	lw $s2, 8($sp)
	lw $s3, 12($sp)
	
	jr $ra
	
	
delay_400_msec:
	addi $sp, $sp -4
	sw $ra, 0($sp)
	
	addi $a0, $zero, 400
	addi $v0, $zero, 32
	syscall
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra
