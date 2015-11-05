
def sher_min(arr,n,p,q):
    	arr.sort()
    	arr1 = []
    	arr2 = []
    
	for i in range(n):
    		arr1.append(abs(arr[i]-p))
		arr2.append(abs(arr[i]-q))

	#print min(arr1)
	#print min(arr2)
	if min(arr1) == min(arr2):
		return p
	elif min(arr1) > min(arr2):
		return p
	elif min(arr2) < min(arr2):
		return q
    
n = int(raw_input())
a = raw_input().split()
a = [int(x) for x in a]
p_q = raw_input().split()
p_q = [int(x) for x in p_q]
p = p_q[0]
q = p_q[1]

print sher_min(a,n,p,q)
