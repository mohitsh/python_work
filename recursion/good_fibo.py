
def good_fibo(n):
	if n <= 1:
		return (n,0)
	else:
		(a,b) = good_fibo(n-1)
		return (a+b,a)

print good_fibo(0)
print good_fibo(1)
print good_fibo(2)
print good_fibo(3)
print good_fibo(4)
print good_fibo(5)
print good_fibo(6)

