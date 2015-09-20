
def binary(array,item):
	first = 0
	last = len(array)-1
	found = False
	while first <= last and not found:
		print "here"
		mid = (first+last)//2
		if array[mid] == item:
			found = True
			return mid
		elif item > array[mid]:
			first = mid+1
		elif item < array[mid]:
			last = mid-1
		else:
			return None


def twosum(nums,target):
	dict = {}
	for i in range(len(nums)):
		key = nums[i]*2654435761%(2**32)
		dict[key] = [i,nums[i]]
	#print dict
	for i in range(len(nums)):
		#print "here"
		j = target-nums[i]
		#print j
		key = j*2654435761%(2**32)
		#print key
		k = dict.get(key)
		if k[0] != i and k != None:
			ans = [i+1,k[0]+1]
			ans.sort()
			return ans

'''
arr = raw_input().split()
narr = [int(x) for x in arr]
target = int(raw_input())
print twosum(narr,target)
'''
arr = [3,2,4]
print twosum(arr,6)

#print binary([1,2,3,4],3)


