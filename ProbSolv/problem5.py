

def plus_minus(n,arr):
	plus_sum = 0
	minus_sum = 0
	zero_sum = 0
	
	for i in range(n):
		if arr[i] == 0:
			zero_sum = zero_sum + 1
		elif arr[i] > 0:
			plus_sum = plus_sum + 1
		elif arr[i] < 0:
			minus_sum = minus_sum + 1
	print "%.3f" % (float(plus_sum)/n)
	print "%.3f" % (float(minus_sum)/n)
	print "%.3f" % (float(zero_sum)/n)



n = int(raw_input())
arr = raw_input().split()
num_arr = [int(x) for x in arr]
#print num_arr
plus_minus(n,num_arr)
