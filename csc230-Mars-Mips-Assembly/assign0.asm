# UVic CSC 230, Summer 2020
#
# Howdy, world!

	.data
howdy_string:
	.asciiz	"\nHello! My name is Naum Hoffman!\n\n"
howdy_number:
	.asciiz "V00927502\n"
	
	
	.text
main:
	li	$v0, 4
	la	$a0, howdy_string
	syscall
	
	li	$v0, 4
	la	$a0, howdy_number
	syscall
	
	li	$v0, 10
	syscall
