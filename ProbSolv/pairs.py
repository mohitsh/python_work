

def binary_search(arr,temp):
	mid = len(arr)/2
	if temp > arr[-1] or temp < arr[0]:
		return False
	if arr[mid] == temp:
		return True
	elif arr[mid] > temp:
		return binary_search(arr[:mid],temp)
	elif arr[mid] < temp:
		return binary_search(arr[mid+1:],temp)
	else:
		return False

def pairs(arr,n,k):
	store = {}
	for i in range(n):
		key = arr[i]*2654435761%(2**32)
		store[key] = arr[i]
		
	count = 0
	for i in range(n):
		temp = arr[i] - k
		key = temp*2654435761%(2**32)
		found = store.get(key)
		if found != None:
			count = count + 1
	print count

#print binary_search([1,2,3,4,5],3)
#print binary_search([1,2,3,4,5],7)	
	
n_k = raw_input().split()
n_k = [int(x) for x in n_k]

n = n_k[0]
k = n_k[1]

arr = raw_input().split()
arr = [int(x) for x in arr]

pairs(arr,n,k)
