

def max_subarray(alist):
	current_sum = 0
	current_index = -1
	best_sum = 0
	best_start_index = -1
	best_end_index = -1

	for i in xrange(len(alist)):
		val = current_sum + alist[i]
		if val > 0:
			if current_sum == 0:
				current_index = i
			current_sum = val
		else:
			current_sum = 0

		if current_sum > best_sum:
			best_sum = current_sum 
			best_start_index = current_index
			best_end_index = i
	return alist[best_start_index:best_end_index+1]
	

print max_subarray([1,-3,5,-2,9,-8,-6,4])
