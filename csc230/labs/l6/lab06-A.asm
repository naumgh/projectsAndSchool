.text
	addi $s3, $zero, 5
loop:
	beq $s3, $zero, finish
	
	jal display_dashes
	jal delay_400_msec
	
	jal display_blanks
	jal delay_400_msec
	
	jal display_digits 
	jal delay_400_msec 
	
	jal display_dashes
	jal delay_400_msec
	
	jal display_blanks
	jal delay_400_msec
	
	addi $s3, $s3, -1
	beq $s3, $0, loop


################
# Display dashes
display_dashes:	
	addi $sp, $sp -4
	sw $ra, 0($sp)
	
	
	la $a0, 0xffff0011
	la $a1, 0xffff0010

	addi $s0, $zero, 0x40
	addi $s1, $zero, 0x40
	
	sb $s0, 0($a0)
	sb $s1, 0($a1)
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	#j loop
	jr $ra



################
# Display blanks
display_blanks:
	addi $sp, $sp, -4
	sw $s0, 0($sp)
	
	la $a0, 0xffff0011
	la $a1, 0xffff0010
	
	addi $s0, $zero, 0x00
	addi $s1, $zero, 0x00
	
	sb $s0 0($a0)
	sb $s1 0($a1)
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	#j loop
	jr $ra
	
	
	
	

################
# Display digits
display_digits:	
	addi $sp, $sp, -4
	sw $s0, 0($sp)
	
	la $a0, 0xffff0011
	la $a1, 0xffff0010
	

	addi $s0, $zero, 0x5b
	addi $s1, $zero, 0x06
	
	
	sb $s0, 0($a0)
	sb $s1, 0($a1)
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	j loop
	jr $ra
	#nop 
	
	


delay_400_msec:
	addi $sp, $sp -4
	sw $ra, 0($sp)
	
	addi $s0, $zero, 400
	addi $v0, $zero, 32
	syscall
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	#j loop
	jr $ra


finish:
	addi $v0, $zero, 10
	syscall
