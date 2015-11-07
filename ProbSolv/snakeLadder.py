
def find_path(arrl,arrs):
	arrl_start = []
	arrl_end = []
	for i in range(len(arrl)):
		arrl_start.append(arrl[i][0])
		arrl_end.append(arrl[i][1])

	print arrl_start
	print arrl_end

	arrs_start = []
	arrs_end = []

	for j in range(len(arrs)):
		arrs_start.append(arrs[j][0])
		arrs_end.append(arrs[j][1])
	
	print arrs_start
	print arrs_end

	path = []
	i = 1
	path.append(i)
	#path.append(i)
	while i<=100:
		if i in arrl_start:
			index = arrl_start.index(i)
			i = arrl_end[index]
		#elif i in arrs_start:
		#	index = arrs_start.index(i)
		#	i = arrs_end[index]
			
		else:
			i = i + 1
		path.append(i)
		#print i
	return path	


l = int(raw_input())
arrl = []
for i in range(l):
	arr1 = raw_input().split()
	arr1 = [int(x) for x in arr1]
	arrl.append(arr1)
s = int(raw_input())
arrs = []
for j in range(s):
	arr1 = raw_input().split()
	arr1 = [int(x) for x in arr1]
	arrs.append(arr1)

#print arrl
#print arrs
ans = find_path(arrl,arrs)
print ans

step = 0
for i in range(1,len(ans)):
	if ans[i] - ans[i-1] != 1:
		step +=1
	





