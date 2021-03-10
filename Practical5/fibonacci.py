def fib_recur(n):
	#to know the nth value of the Fibonacci sequence
	assert n>=0
	if n in (0,1):
		return n
	return fib_recur(n-1)+fib_recur(n-2)
	
for i in range(14):
	#to compute and display the first 14 values of the Fibonacci sequence
	#the 14th value of the sequence is the result we want
	print(fib_recur(i), end=" ")
	
