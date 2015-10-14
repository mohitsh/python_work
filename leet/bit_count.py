



def bit_count(n):
	count = 0
	while n > 0:
		count = count + 1
		n=n&(n-1)
	return count

#a = int('11101',2)
#print bit_count(a)


def acm(arr):
	for i in range(len(arr)):
		for j in range(i):
			


n = int(raw_input())
m = int(raw_input())

arr = []
for i in range(n):
	a = int(str(raw_input()),2)
	arr.append(a)
print arr

	
