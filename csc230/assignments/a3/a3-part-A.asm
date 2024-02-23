
	.data
ARRAY_A:
	.word	21, 210, 49, 4
ARRAY_B:
	.word	21, -314159, 0x1000, 0x7fffffff, 3, 1, 4, 1, 5, 9, 2
ARRAY_Z:
	.space	28
NEWLINE:
	.asciiz "\n"
SPACE:
	.asciiz " "
		
	
	.text  
main:	
	la $a0, ARRAY_A
	addi $a1, $zero, 4
	jal dump_array
	
	
	
	la $a0, ARRAY_B
	addi $a1, $zero, 11
	jal dump_array
	

	la $a0, ARRAY_Z
	lw $t0, 0($a0)
	addi $t0, $t0, 1
	sw $t0, 0($a0)
	addi $a1, $zero, 9
	jal dump_array
	
	addi $v0, $zero, 10
	syscall
	

# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	
	
dump_array:
	#zet i to zero 
	add $t0, $zero, $zero
	
	#saving value of $a0 into $s0
	add $s0, $a0, $zero
	dump_array_while:
		
		
		#calculate offset
		mul $t2, $t0, 4
		
		
		#adding offset by starting address of array
		add $t2, $t2, $s0
		#loading word from offset array into $t1
		lw $t1, ($t2)
		#printing value
		addi $v0, $zero, 1
		add $a0, $t1, $zero
		syscall
		
		#printing SPACE
		addi $v0, $zero, 4
		la $a0, SPACE 
		syscall 		
		
		#i++
		addi $t0, $t0, 1
		
		
		#compare max with i
		blt $t0, $a1, dump_array_while
	
	
	addi $v0, $zero, 4
	la $a0, NEWLINE
	syscall
	jr $ra
	
	
	
	
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE
