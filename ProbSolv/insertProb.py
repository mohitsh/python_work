
def func(arr,n):
	for i in range(n-1,-1,-1):
		if arr[i-1] < arr[i]:
			arr[i] = arr	

n = int(raw_input())
a = raw_input().split()
arr = [int(x) for x in a]
func(arr,n)
