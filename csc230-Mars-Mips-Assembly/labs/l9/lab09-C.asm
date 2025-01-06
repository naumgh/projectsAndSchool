
	.data
	.eqv  BITMAP_DISPLAY 0x10010000
	.eqv  PIXEL_WHITE    0x00ffffff
	
	.text
	
	la $s0, BITMAP_DISPLAY
	li $s1, PIXEL_WHITE
	
	# Draw a row of white pixels on the bitmap display tool
	# Use row 4. You will need to write a loop!
	
	#drawing the row
	addi $s0, $s0, 320
	addi $a1, $zero, 0x1001017C
	sw $s1, 0($s0)		# This is not the correct value!
	
	while0:
		addi $s0, $s0, 4
		sw $s1, 0($s0)
		blt $s0, $a1, while0

		
	
	#clearing out s0
	add $s0, $zero, $zero
	add $a1, $zero, $zero
	
	# Draw a column of white pixels on the bitmap display tool
	# Use column 3. You will need to write a loop!
	
	#drawing the column
	la $s0, BITMAP_DISPLAY
	addi $s0, $s0, 12
	addi $a1, $zero, 0x100103D8
	sw $s1, 0($s0)		# This is not the correct value!
	
	while:
		addi $s0, $s0, 64
		sw $s1, 0($s0)
		blt $s0, $a1, while

	addi $v0, $zero, 10
	syscall
