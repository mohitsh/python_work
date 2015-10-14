
n = int(raw_input())
arr1 = raw_input().split()
arr = [int(x) for x in arr1]



def calc(a,b):
	ans = (((a and b) ^ (a or b)) and (a ^ b))
	return ans

dude = []
for i in range(n):
	for j in range(i):
		ans = calc(arr[i],arr[j])
		dude.append(ans)

print max(dude)
