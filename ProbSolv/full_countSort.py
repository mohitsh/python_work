

def find(v,n,arr):
	for i in range(n):
		if arr[i] == v:
			return i


v = int(raw_input())
n = int(raw_input())
arr  = raw_input().split()
arr = [int(x) for x in arr]
print find(v,n,arr)


