.text 
	# $8 : initial value for which we look for trailing zeros
	# $9 : the counter to keeps track of # of trailing zeros (result)
	# $10 :  the result of the AND with the mask
	
	ori $8, $0, 0	# same as "addi $8, $0, 0xc800"
	
	ori $9, $0, 0		# counter
loop:
	andi $10, $8, 1
	bne $10, $0, exit
	addi $9, $9, 1
	srl $8, $8, 1
	b loop
	
exit:
	nop			# answer is in $9
	
	
#the fatal flaw is that if the value is 0, it will run forever
#creating an infinite loop and eventually crashing.
# This is because after the bits are shifted,
#a zero is added on the left. The program only stops when it sees a 1.
#we can fix this by adding a case that states if there are no ones in
#the code, then the trailing bits must be 1.