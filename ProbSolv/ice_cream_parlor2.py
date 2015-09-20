

def ice_cream_parlor(m,n,arr):
	i = 0
	j = n-1
	while i < n:
		while arr[i] + arr[j] > m and j > 0:
			j = j-1
		if arr[i] + arr[j] == m:
			dude = [i+1,j+1]
			dude.sort()
			return ' '.join([str(x) for x in dude])
		i = i + 1
			



t = int(raw_input())
for i in range(t):
        m = int(raw_input())
        n = int(raw_input())
        #a = raw_input().split()
        #arr = [int(x) for x in a]
	inp = map(int,raw_input().split())
	print ice_cream_parlor(m,n,inp)

