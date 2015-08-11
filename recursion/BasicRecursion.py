
# doing List Sum normal way by using for loop
def ListSum(alist):
	count = 0
	for i in range(len(alist)):
		count = count + alist[i]
	return count

print ListSum([1,2,3,4,5])
print ListSum([1,2,3])

# same List Sum using recursion
def ListSumRecur(alist):
	if len(alist) == 1:
		return alist[0]
	else:
		return alist[0] + ListSumRecur(alist[1:])

print ListSumRecur([1,2,3,4,5])
print ListSumRecur([1,2,3])


def factorial(num):
	if num <= 1:
		return 1
	else:
		return num*factorial(num-1)

print factorial(5)
print factorial(6)
print factorial(4)

