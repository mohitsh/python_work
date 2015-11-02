

def jim_orders(arr,n):
	arr1 = []
	dude = []
	for i in range(n):
		arr1.append(sum(arr[i]))
		dude.append(sum(arr[i]))
	arr1.sort()
	arr3 = []
	for elem in arr1:
		arr3.append((dude.index(elem))+1)
	arr3 = [str(x) for x in arr3]
	print " ".join(arr3)


n = int(raw_input())
arr = []
for i in range(n):
	arr1 = raw_input().split()
	arr1 = [int(x) for x in arr1]
	arr.append(arr1)

jim_orders(arr,n)
