

def bad_fibo(n):
	if n <= 1:
		return 1
	else:
		return bad_fibo(n-1) + bad_fibo(n-2)

print bad_fibo(0)
print bad_fibo(1)
print bad_fibo(2)
print bad_fibo(3)
print bad_fibo(4)
print bad_fibo(5)
print bad_fibo(6)
