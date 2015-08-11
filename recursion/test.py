
def listSum(alist):
	if len(alist) == 1:
		return alist[0]
	else:
		return alist[0] + listSum(alist[1:])

print listSum([1,2,3,4,5])
print listSum([100])



def fact(num):
	if num <= 1:
		return 1
	else:
		return num*fact(num-1)
print fact(1)
print fact(2)
print fact(3)
print fact(4)
print fact(5)

		
