

def fib(first,second,n):
	if n == 2:
		return (second,first)
	else:
		(a,b) = fib(first,second,n-1)
		return ((a*a)+b,a)


#print fib(0,1,5)
inp = raw_input().split()
arr = [int(x) for x in inp]
print fib(arr[0],arr[1],arr[2])[0]
