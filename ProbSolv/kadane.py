


def max_subarray(alist):
	max_end_here  = alist[0]
	max_so_far = alist[0]
	for x in alist[1:]:
		max_end_here = max(x,max_end_here+x)
		max_so_far = max(max_so_far, max_end_here)
	return max_so_far

alist = [-2,1,-3,4,-1,2,1,-5,4]
print max_subarray(alist) 
