def fibonacci(x):
	if (x <= 1):
		return x
	else:
		return(fibonacci(x-1) + fibonacci(x-2))
x = int(input('Enter number:'))

print ('fibonacci numbers:')
for i in range(x):
	print fibonacci(i),
