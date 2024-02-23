x = 8

def fn():
	print(x)

def fn1(x):
	print(x)
	x = x + 1
	print(x)

def fn2():
	global x
	print(x)
	x = x + 2
	print(x)

def fn3(x):
	print(x)
	x = x + 3
	print(x)
	return x

def main():
	fn()
	print(x)
	fn1(0)
	print(x)
	fn2()
	print(x)
	print(fn3(x))

main()
