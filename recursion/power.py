

def power(x,n):
	if n == 0:
		return 1
	else:
		return x*power(x,n-1)

print power(2,0)
print power(2,1)
print power(2,2)
print power(2,3)
print power(2,4)
print power(2,5)


def power2(x,n):
	if n == 0:
		return 1
	elif n%2 != 0:
		return x*(power2(x,n//2)**2)
	elif n%2 == 0:
		return power2(x,n//2)**2

print power(2,0)
print power(2,1)
print power(2,2)
print power(2,3)
print power(2,4)
print power(2,5)


